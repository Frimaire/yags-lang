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
// the existed yags-compiler
var BUILDPATH = '.';
var DSTPATH = './n';
var DUMP_AST = false;
var DUMP_IR = false;

var {mkdir} = import('os');
var {join: joinPath, dirname, basename, isdir, normpath} = import('os.path');
var {time} = import('time');
var {version_info: pyver} = import('sys');
var {ArgumentParser} = import('argparse');
var {dumps: json_stringify} = import('json');
var {copyfile, copytree} = import('shutil');
var subprocess = import("subprocess");

// the file extension to be compiled
var SRC_SUFFIX = '.as';
// 0 - compile (.as), 1 - copy .py, 2 - copy directory, {} - subdirectory
var SRC_TREE = {
    parser: 2,
    tools: {
        cas: 0,
        esstring: 1,
        range: 1,
        options: 1,
        __init__: 1
    },
    ir: {
        ast2ir: 0,
        element: 0,
        pygen: 0,
        symboltree: 0,
        attribute: 0,
        variable: 0,
        StringMap: 0,
        utils: 0,
        compat: 1,
        syntax: 1,
        __init__: 1
    },
    compile: 0,
    bootstrap: 0
};

// mkdir for new version
[DSTPATH, joinPath(DSTPATH, 'cc1'), joinPath(DSTPATH, 'cc2'), joinPath(DSTPATH, 'cc3')].@forEach(function(p, _) {
    try {
        mkdir(p);
    } catch(errsc) {
        print('Cannot create the directory %s for new compilers. If the directory already exists, please delete it manually at first.' % p);
        exit(1);
    }
});

var time_st = time();

// use stage 0 (existed) compiler
print("Stage 1");
process('..', 'cc1');

print("Stage 2");
// switch to stage 1 ir
process('cc1', 'cc2');

print("Stage 3");
// switch to stage 2 ir
process('cc2', 'cc3');

// comparison of the stage1 and stage2 compilers
print("verifying 1 and 2 (for reference only)...");
docompare('cc1', 'cc2');

print("verifying...");
var v = docompare('cc2', 'cc3');
if(!v) {
    print("something goes wrong");
    exit(1);
} else {
    print("all correct");
}

var finalbase = joinPath(DSTPATH, 'cc3');

var clean_sh = [];
// delete AST, IR
clean_sh.append('find "' + finalbase + '" -name "*.json" -type f -delete');
clean_sh.append('find "' + finalbase + '" -name "*.xml" -type f -delete');
// replace the old compiler
SRC_TREE.@forEach(function(name, _) {
    var t = SRC_TREE[name];
    name = name + (t === 0 || t === 1 ? '.py' : '');
    clean_sh.append('rm -rf "' + BUILDPATH + '/' + name + '"');
    clean_sh.append('mv "' + finalbase + '/' + name + '" "' + BUILDPATH + '/' + name + '"');
});
// clean-up
clean_sh.append('rm -rf "' + DSTPATH + '"');
clean_sh.append('rm $0');

var clean_sh_file = open(joinPath('.', 'cleanandreplace.sh'), 'wb');
try {
    clean_sh_file.write(clean_sh.@join('\n').encode('utf-8'));
} finally {
    clean_sh_file.close();
}
print('Done. If everything is OK, run cleanandreplace.sh to delete the older version.');

var time_sp = time();
print("Total time consumption: %f s" % (time_sp - time_st));

function copypy(srcdir, dstdir, modname) {
    var srcpath = joinPath(srcdir, modname + '.py');
    var dstpath = joinPath(dstdir, modname + '.py');
    print('copy: ' + srcpath + ' -> ' + dstpath);
    copyfile(srcpath, dstpath);
}

function docompile(compilerpath, srcpath, dstpath) {
    print('compile: ' + srcpath + ' -> ' + dstpath);
    var args = ['python3', compilerpath, '-o', dstpath, srcpath];
    if(DUMP_AST) {
        args.append('--dump-ast');
    }
    if(DUMP_IR) {
        args.append('--dump-ir');
    }
    try {
        subprocess.check_output(args);
    } catch(e) {
        if(e instanceof subprocess.CalledProcessError) {
            print('compilation failed, compiler returns %d' % e.returncode);
        } else {
            print('compilation failed: %s' % str(e));
        }
        exit(1);
    }
}

function process(compilerref, dstname) {
    var time_st = time();
    var compilerbase = joinPath(DSTPATH, compilerref);
    var compilerpath = joinPath(compilerbase, "compile.py");
    print("build: " + dstname + ", using " + compilerpath);
    var dstbase = joinPath(DSTPATH, dstname);
    // process the src tree
    walk(function(dirpath, name, v) {
        // 0 - compile (.as), 1 - copy .py, 2 - copy directory
        // null - directory
        var srcpath, dstpath;
        if(v === null) {
            // make sub dir
            dstpath = joinPath(dstbase, dirpath);
            print("mkdir: " + dstpath);
            mkdir(dstpath);
            return;
        }
        if(v == 2) {
            // copy the directory recursive
            srcpath = joinPath(SRCPATH, dirpath, name);
            dstpath = joinPath(dstbase, dirpath, name);
            print(srcpath + " -> " + dstpath);
            copytree(srcpath, dstpath);
            return;
        }
        if(v === 1) {
            // copy the python files
            srcpath = joinPath(SRCPATH, dirpath);
            dstpath = joinPath(dstbase, dirpath);
            copypy(srcpath, dstpath, name);
            return;
        }
        if(v === 0) {
            // compile yags
            srcpath = joinPath(SRCPATH, dirpath, name + SRC_SUFFIX);
            dstpath = joinPath(dstbase, dirpath, name + '.py');
            docompile(compilerpath, srcpath, dstpath);
            return;
        }
        throw new TypeError("Don't know how to process " + str(dirpath) + "/" + str(name));
    });
    var time_sp = time();
    print("Time consumption in this stage: %f s" % (time_sp - time_st));
}

function readall(path) {
    var fp = open(path, 'r');
    try {
        return fp.read();
    } finally {
        fp.close;
    }
}

function docompare(base1, base2) {
    var dstbase1 = joinPath(DSTPATH, base1);
    var dstbase2 = joinPath(DSTPATH, base2);
    print("compare " + dstbase1 + " == " + dstbase2);
    var v = true;
    walk(function(path, fn, typ) {
        if(typ !== 0) {
            return;
        }
        var distpath = joinPath(dstbase1, path, fn + ".py");
        var dstpath = joinPath(dstbase2, path, fn + ".py");
        var dist = readall(distpath);
        var dst = readall(dstpath);
        var f = dist === dst;
        print(fn + " " + (f ? "verified" : "differs"));
        v = v && f;
    });
    return v;
}

// call cb(srcdirpath, name, value)
function walk(cb) {
    doWalk('.', SRC_TREE, cb);
}

function doWalk(p, d, cb) {
    d.@forEach(function(k, _) {
        // py's dict iters the key
        var v = d[k];
        if(v instanceof dict) {
            var dd = joinPath(p, k);
            cb(dd, null, null);
            doWalk(dd, v, cb);
            return;
        }
        cb(p, k, v);
    });
}

