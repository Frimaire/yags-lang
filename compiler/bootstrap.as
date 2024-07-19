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

/**
 * a 3-stage bootstrap script used to upgrade the compiler
 */

var SRCPATH = '..';
var DUMP_AST = false;
var DUMP_IR = false;

var {mkdir} = import('os');
var {join, dirname, basename, isdir, normpath} = import('os.path');
var {time} = import('time');
var {version_info: pyver} = import('sys');
var {ArgumentParser} = import('argparse');
var {dumps: json_stringify} = import('json');
var {copyfile} = import('shutil');

// the parser
var {parse, toDict} = import('parser.esprima');

// use stage 0 (existed) compiler
var {convertASTIR} = import('ir.ast2ir');
var {XMLDumper} = import('ir.utils');
var {PyGenerator} = import('ir.pygen');
var {StringMap} = import('ir.StringMap');

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

function process(srcdir, dstdir, modname, dump = false, dast = false, options = null) {
    var srcpath = join(srcdir, modname + '.as');
    var dstpath = join(dstdir, modname + '.py');
    print(srcpath + ' -> ' + dstpath);
    
    var srcf = open(srcpath, 'rb');
    try {
        var ascode = srcf.read().decode('utf-8');
    } finally {
        srcf.close();
    }

    // the base path of the dump files
    var dfn = dstpath.@slice(-3) === '.py' ? dstpath.@slice(0, -3) : dstpath;
    
    var ast = parse.@apply([ascode], {
        options: {
            'attachComment': true,
            'loc': true,
            'range': true
        }
    });
    dumpAST(ast, dfn + '-ast.json', dast);

    var ir = convertASTIR(ast, options);
    try {
        ir.checkAllStructure();
        dumpIR(ir, dfn + '-initial.xml', dump);

        ir.declareVariable();
        ir.checkAllStructure();
        dumpIR(ir, dfn + '-declare-variable.xml', dump);

        ir.checkVariables();
        ir.checkAllStructure();
        dumpIR(ir, dfn + '-check-variable.xml', dump);

        ir.functionalize();
        ir.checkAllStructure();
        dumpIR(ir, dfn + '-functionalize.xml', dump);

        ir.simplifyExpressions();
        ir.checkAllStructure();
        dumpIR(ir, dfn + '-simplify-expressions.xml', dump);
    } finally {
        dumpIR(ir, dfn + '-current.xml', dump);
    }

    var gen = new PyGenerator();
    ir.generatePython(gen);
    var pytxt = gen.finalize();

    var pyf = open(dstpath, 'wb');
    try {
        pyf.write(pytxt.encode('utf-8'));
    } finally {
        pyf.close();
    }
}

function copypy(srcdir, dstdir, modname) {
    var srcpath = join(srcdir, modname + '.py');
    var dstpath = join(dstdir, modname + '.py');
    print(srcpath + ' -> ' + dstpath);
    copyfile(srcpath, dstpath);
}

function readall(path) {
    var fp = open(path, 'r');
    try {
        return fp.read();
    } finally {
        fp.close;
    }
}

var time_st = time();

// mkdir for new version script
var dstscriptdir = join('.', 'scripts-n');
try {
    mkdir(dstscriptdir);
} catch(errsc) {
    print('Cannot create the directory for compiler scripts (scripts-n). If the directory already exists, please delete it manually at first.');
    exit();
}

// the files to be compiled
var src_list = ["ast2ir", "element", "pygen", "symboltree", 
                 "identifier", "StringMap", "utils"];

// the files to be copied
var py_list = ["compat", "syntax", "__init__"];

print("Stage 1");
var srcirdir = join(SRCPATH, 'ir');
var dstirdir = join('.', 'ir1');
// mkdir
try {
    mkdir(dstirdir);
} catch(err1) {
    print('Cannot create the directory for stage 1 ir. If the directory already exists, please delete it manually at first.');
    exit();
}
src_list.@forEach(function(fn, k) {
    process(srcirdir, dstirdir, fn, DUMP_IR, DUMP_AST);
});
py_list.@forEach(function(fn, k) {
    copypy(srcirdir, dstirdir, fn);
});

print("Stage 2");
// switch to stage 1 ir
({convertASTIR}) = import('ir1.ast2ir');
({XMLDumper}) = import('ir1.utils');
({PyGenerator}) = import('ir1.pygen');
({StringMap}) = import('ir1.StringMap');
dstirdir = join('.', 'ir2');
var dstirdir2 = dstirdir;
// mkdir
try {
    mkdir(dstirdir);
} catch(err2) {
    print('Cannot create the directory for stage 2 ir. If the directory already exists, please delete it manually at first.');
    exit();
}
src_list.@forEach(function(fn, k) {
    process(srcirdir, dstirdir, fn, DUMP_IR, DUMP_AST);
});
py_list.@forEach(function(fn, k) {
    copypy(srcirdir, dstirdir, fn);
});

print("Stage 3");
// switch to stage 2 ir
({convertASTIR}) = import('ir2.ast2ir');
({XMLDumper}) = import('ir2.utils');
({PyGenerator}) = import('ir2.pygen');
({StringMap}) = import('ir2.StringMap');
dstirdir = join('.', 'ir3');
var dstirdir3 = dstirdir;
// mkdir
try {
    mkdir(dstirdir);
} catch(err3) {
    print('Cannot create the directory for stage 3 ir. If the directory already exists, please delete it manually at first.');
    exit();
}
src_list.@forEach(function(fn, k) {
    process(srcirdir, dstirdir, fn, DUMP_IR, DUMP_AST);
});
py_list.@forEach(function(fn, k) {
    copypy(srcirdir, dstirdir, fn);
});

// comparison of the stage2 and stage3 compilers
print("verifying...");
var v = true;
src_list.@forEach(function(fn, k) {
    var distpath = join(dstirdir2, fn + ".py");
    var dstpath = join(dstirdir3, fn + ".py");
    var dist = readall(distpath);
    var dst = readall(dstpath);
    var f = dist === dst;
    v = v && f;
    print(fn + " " + (f ? "verified" : "differs"));
});
print(v ? "all correct" : "something goes wrong");

// compile new compile.py and bootstrap.py
process(SRCPATH, dstscriptdir, 'compile', DUMP_IR, DUMP_AST);
process(SRCPATH, dstscriptdir, 'bootstrap', DUMP_IR, DUMP_AST);

var clean_sh = 'rm -rf parser/__pycache__\n\
rm -rf ir\n\
rm -rf ir1\n\
rm -rf ir2\n\
rm ir3/*.xml\n\
rm ir3/*.json\n\
mv ir3 ir\n\
mv scripts-n/compile.py ./compile.py\n\
mv scripts-n/bootstrap.py ./bootstrap.py\n\
rm -rf scripts-n\n\
rm $0';
var clean_sh_file = open(join('.', 'cleanandreplace.sh'), 'wb');
try {
    clean_sh_file.write(clean_sh.encode('utf-8'));
} finally {
    clean_sh_file.close();
}
print('Done. If everything is OK, run cleanandreplace.sh to delete the older version.');

var time_sp = time();
print("Time cost: %f s" % (time_sp - time_st));
