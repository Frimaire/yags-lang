/* Copyright 2024 Frimaire and other contributors
 * 
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * 
 *     http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

var {time} = import('time');
var timeStart = time();

var {join, dirname, basename, isdir, normpath} = import('os.path');
var {version_info: pyver} = import('sys');
var {ArgumentParser} = import('argparse');
var {dumps: json_stringify} = import('json');
var {parse, toDict} = import('parser.esprima');
var {convertASTIR} = import('ir.ast2ir');
var {XMLDumper} = import('ir.utils');
var {PyGenerator} = import('ir.pygen');
var {StringMap} = import('ir.StringMap');
var {CompileError, init: initAlert, error, note} = import('tools.cas');
var {options} = import('tools.options');

var timeLoaded = time();

var version = "0.2";

function dumpIR(ir, path = 'unknown-current.xml', action = true) {
    if(!action) {
        return;
    }
	var dmp = new XMLDumper();
    var irxml = ir.dump(dmp);
    var xmlhead = '<?xml version="1.0" encoding="UTF-8"?>\n';
    var xmltxt = xmlhead + dmp.toString();
    var f = open(path, 'wb');
    try {
        f.write(xmltxt.encode('utf-8'));
    } finally {
        f.close();
    }
}

function dumpAST(ast, path = 'unknown-ast.json', action = true) {
    if(!action) {
        return;
    }
    var asttxt = json_stringify.@apply([toDict(ast)], {
        indent: 4
    });
    var f = open(path, 'wb');
    try {
        f.write(asttxt.encode('utf-8'));
    } finally {
        f.close();
    }
}

var timeReaded, timeParse, timeConvIR, timeDecl, timeCheck, timeFunc, timeSimp;

/**
 * Read the yags source from srcpath and write the compiled Python code to dstdir/dstname.py
 * @param {String} srcpath, the path of the input
 * @param {String} dstpath, the path of the output
 * @param {Boolean} dump, true if the IR XML should be dumped into output directory
 * @param {Boolean} dast, true if the AST should be dumped into output directory
 */
function process(srcpath, dstpath, dump = false, dast = false) {
    initAlert(srcpath, null);
    
    var srcf = null;
    try {
        srcf = open(srcpath, 'rb');
        var ascode = srcf.read().decode('utf-8');
    } catch(iferr) {
        error('Can not open the input file: %s', str(iferr));
    } finally {
        if(srcf !== null) {
            srcf.close();
        }
    }
    
    initAlert(srcpath, ascode);

    // the base path of the dump files
    var dfn = dstpath.@slice(-3) === '.py' ? dstpath.@slice(0, -3) : dstpath;
    timeReaded = time();
    
    var ast = parse.@apply([ascode], {
        options: {
            'attachComment': true,
            'loc': true,
            'range': true
        }
    });
    dumpAST(ast, dfn + '-ast.json', dast);
    timeParse = time();

    var ir = convertASTIR(ast);
    timeConvIR = time();
    
    try {
        ir.checkAllStructure();
        dumpIR(ir, dfn + '-initial.xml', dump);

        ir.declareVariable();
        ir.checkAllStructure();
        dumpIR(ir, dfn + '-declare-variable.xml', dump);
        timeDecl = time();

        ir.checkVariables();
        ir.checkAllStructure();
        dumpIR(ir, dfn + '-check-variable.xml', dump);
        timeCheck = time();

        ir.functionalize();
        ir.checkAllStructure();
        dumpIR(ir, dfn + '-functionalize.xml', dump);
        timeFunc = time();

        ir.simplifyExpressions();
        ir.checkAllStructure();
        dumpIR(ir, dfn + '-simplify-expressions.xml', dump);
        timeSimp = time();
    } finally {
        dumpIR(ir, dfn + '-current.xml', dump);
    }

    var gen = new PyGenerator();
    ir.generatePython(gen);
    var pytxt = gen.finalize();
    
    var pyf = null;
    try {
        pyf = open(dstpath, 'wb');
        pyf.write(pytxt.encode('utf-8'));
    } catch(oferr) {
        error('Can not open the output file: %s', str(oferr));
    }  finally {
        if(pyf !== null) {
            pyf.close();
        }
    }
}

var argp = new ArgumentParser('yags', null, 'Compile YAGS to Python code');
function aarg(argv, o) {
    argp.add_argument.@apply(argv, o);
}
aarg(['-v', '--version'], {
    action: 'version',
    version: 'YAGS compiler %s (on Python %d.%d)' % tuple([version, pyver.major, pyver.minor])
});

aarg(['-o', '--output'], {
    action: 'store',
    dest: 'dstpath',
    metavar: 'OUTPUT_FILE',
    help: 'Specify the path of output file. If this is not specified, the same directory as the input will be used as the output directory.'
});
aarg(['input'], {
    action: 'store',
    metavar: 'INPUT_FILE',
    help: 'Specify the path of input file.'
});

aarg(['--enable-implicit-bool'], {
    action: 'store_true',
    dest: 'enableImplicitBooleanConversion',
    help: 'Enable experimental implicit boolean conversion.'
});
aarg(['--enable-tuple-subscription'], {
    action: 'store_true',
    dest: 'enableTupleSubscription',
    help: 'Enable experimental tuple subscription. That is, allow comma-separated expressions in the object[expressions] syntax, which will be converted to a tuple. This feature is used to facilitate the access of some multidimensional arraies such as numpy.ndarray.'
});
aarg(['--dump-ir'], {
    action: 'store_true',
    dest: 'allowDumpIR',
    help: 'Dump the intermediate representation as XML into the output directory.',
});
aarg(['--dump-ast'], {
    action: 'store_true',
    dest: 'allowDumpAST',
    help: 'Dump the syntax tree as JSON into the output directory.'
});
aarg(['--trace-profile'], {
    action: 'store_true',
    dest: 'traceProfile',
    help: 'Show the time used for each stage.'
});

var {
    allowDumpIR, allowDumpAST, dstpath, input: srcpath,
    enableImplicitBooleanConversion, enableTupleSubscription,
    traceProfile
} = argp.parse_args();

var timeArgParsed = time();

options.enableImplicitBooleanConversion = enableImplicitBooleanConversion;
options.enableTupleSubscription = enableTupleSubscription;

// get the output name and directory
srcpath = normpath(srcpath);
if(dstpath === null) {
    var fn = basename(srcpath);
    fn = (fn.@slice(-5) === '.yags' ? fn.@slice(0, -5) : (fn.@slice(-3) === '.as' ? fn.@slice(0, -3) : fn)) + '.py';
    dstpath = join(dirname(srcpath), fn);
}

try {
    process(srcpath, dstpath, allowDumpIR, allowDumpAST);
} catch(ce) {
    if(ce instanceof CompileError) {
        print('compilation terminated');
        exit(1);
    } else {
        throw ce;
    }
}
var timeFin = time();
if(traceProfile) {
    note("Time used:");
    note("Load: %.3f s", timeLoaded - timeStart);
    note("Get options: %.3f s", timeArgParsed - timeLoaded);
    note("Read input: %.3f s", timeReaded - timeArgParsed);
    note("Parse: %.3f s", timeParse - timeReaded);
    note("Convert to IR: %.3f s", timeConvIR - timeParse);
    note("Declare variables: %.3f s", timeDecl - timeConvIR);
    note("Check variables: %.3f s", timeCheck - timeDecl);
    note("Functionalize: %.3f s", timeFunc - timeCheck);
    note("Simplify: %.3f s", timeSimp - timeFunc);
    note("Generate Python: %.3f s", timeFin - timeSimp);
    note("Total: %.3f s", timeFin - timeStart);
}
