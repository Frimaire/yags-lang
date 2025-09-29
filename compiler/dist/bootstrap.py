# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, division, generators

__all__ = ()


def __():
    from libyags0 import __x_tup, __x_tupof, __x_lst, __x_errT, __x_eq, __x_ne, __x_typ, __x_cb, __x_not, __x_iof, __x_inc, __x_dec, __x_var, __x_imf, __x_at_take, __x_at_drop, __x_at_forEach, __x_at_map, __x_at_filter, __x_at_flatMap, __x_at_some, __x_at_every, __x_at_find, __x_at_findIndex, __x_at_reduce, __x_at_join, __x_at_bind, __x_at_apply, __x_at_length, __x_at_isEmpty, __x_at_push, __x_at_pop, __x_at_shift, __x_at_unshift, __x_at_slice, __x_at_splice, __x_at_has, __x_dcls, __x_dpif, __x_dpsf, __x_prmT, __x_csgT, __x_cpgT, __x_objT, __x_smet, __x_prop, __x_tob, __x_tnb, Infinity, NaN
    __x_imp = __x_imf(__name__)

    # function definitions:

    def copypy(srcdir, dstdir, modname):
        srcpath = joinPath(srcdir, modname + (u".py"))
        dstpath = joinPath(dstdir, modname + (u".py"))
        print((u"copy: ") + srcpath + (u" -> ") + dstpath)
        copyfile(srcpath, dstpath)
    # end function copypy

    def docompile(compilerpath, srcpath, dstpath):
        print((u"compile: ") + srcpath + (u" -> ") + dstpath)
        args = [(u"python3"), compilerpath, (u"-o"), dstpath, srcpath]
        if __x_cb(DUMP_AST):
            args.append((u"--dump-ast"))
        # end if
        if __x_cb(DUMP_IR):
            args.append((u"--dump-ir"))
        # end if
        try:
            subprocess.check_output(args)
        except __x_errT as e:
            if __x_cb(__x_iof(e, subprocess.CalledProcessError)):
                print((u"compilation failed, compiler returns %d") % e.returncode)
            else:
                print((u"compilation failed: %s") % str(e))
            # end if
            exit(1)
        # end try
    # end function docompile

    def process(compilerref, dstname):
        def __f4_(dirpath, name, v):
            if __x_cb(__x_eq(v, None)):
                dstpath = joinPath(dstbase, dirpath)
                print((u"mkdir: ") + dstpath)
                mkdir(dstpath)
                return
            # end if
            if __x_cb(v == 2):
                srcpath = joinPath(SRCPATH, dirpath, name)
                dstpath = joinPath(dstbase, dirpath, name)
                print(srcpath + (u" -> ") + dstpath)
                copytree(srcpath, dstpath)
                return
            # end if
            if __x_cb(__x_eq(v, 1)):
                srcpath = joinPath(SRCPATH, dirpath)
                dstpath = joinPath(dstbase, dirpath)
                copypy(srcpath, dstpath, name)
                return
            # end if
            if __x_cb(__x_eq(v, 0)):
                srcpath = joinPath(SRCPATH, dirpath, name + SRC_SUFFIX)
                dstpath = joinPath(dstbase, dirpath, name + (u".py"))
                docompile(compilerpath, srcpath, dstpath)
                return
            # end if
            raise TypeError((u"Don't know how to process ") + str(dirpath) + (u"/") + str(name))
        # end function <anonymous> (__f4_)

        time_st = time()
        compilerbase = joinPath(DSTPATH, compilerref)
        compilerpath = joinPath(compilerbase, (u"compile.py"))
        print((u"build: ") + dstname + (u", using ") + compilerpath)
        dstbase = joinPath(DSTPATH, dstname)
        walk(__f4_)
        time_sp = time()
        print((u"Time consumption in this stage: %f s") % (time_sp - time_st))
    # end function process

    def readall(path):
        fp = open(path, (u"r"))
        try:
            return fp.read()
        finally:
            fp.close
        # end try
    # end function readall

    def docompare(base1, base2):
        def __f7_(path, fn, typ):
            if __x_cb(__x_ne(typ, 0)):
                return
            # end if
            distpath = joinPath(dstbase1, path, fn + (u".py"))
            dstpath = joinPath(dstbase2, path, fn + (u".py"))
            dist = readall(distpath)
            dst = readall(dstpath)
            f = __x_eq(dist, dst)
            print(fn + (u" ") + ((u"verified") if __x_cb(f) else (u"differs")))
            __u_v.val = __x_cb(__u_v.val) and f
        # end function <anonymous> (__f7_)

        __u_v = __x_var()
        dstbase1 = joinPath(DSTPATH, base1)
        dstbase2 = joinPath(DSTPATH, base2)
        print((u"compare ") + dstbase1 + (u" == ") + dstbase2)
        __u_v.val = True
        walk(__f7_)
        return __u_v.val
    # end function docompare

    def walk(cb):
        doWalk((u"."), SRC_TREE, cb)
    # end function walk

    def doWalk(p, d, cb):
        def __fA_(k, _):
            v = d[k]
            if __x_cb(__x_iof(v, dict)):
                dd = joinPath(p, k)
                cb(dd, None, None)
                doWalk(dd, v, cb)
                return
            # end if
            cb(p, k, v)
        # end function <anonymous> (__fA_)

        __x_at_forEach(d, __fA_)
    # end function doWalk

    def __fB_(p, _):
        try:
            mkdir(p)
        except __x_errT as errsc:
            print((u"Cannot create the directory %s for new compilers. If the directory already exists, please delete it \
manually at first.") % p)
            exit(1)
        # end try
    # end function <anonymous> (__fB_)

    def __fC_(name, _):
        t = SRC_TREE[name]
        name = name + ((u".py") if __x_cb(__x_cb(__x_eq(t, 0)) or __x_eq(t, 1)) else (u""))
        clean_sh.append((u"rm -rf \"") + BUILDPATH + (u"/") + name + (u"\""))
        clean_sh.append((u"mv \"") + finalbase + (u"/") + name + (u"\" \"") + BUILDPATH + (u"/") + name + (u"\""))
    # end function <anonymous> (__fC_)

    # class definitions:

    SRCPATH = (u"..")
    BUILDPATH = (u".")
    DSTPATH = (u"./n")
    DUMP_AST = False
    DUMP_IR = False
    __r0 = __x_imp((u"os"))
    mkdir = __r0.mkdir
    __r1 = __x_imp((u"os.path"))
    joinPath = __r1.join
    dirname = __r1.dirname
    basename = __r1.basename
    isdir = __r1.isdir
    normpath = __r1.normpath
    __r2 = __x_imp((u"time"))
    time = __r2.time
    __r3 = __x_imp((u"sys"))
    pyver = __r3.version_info
    __r4 = __x_imp((u"argparse"))
    ArgumentParser = __r4.ArgumentParser
    __r5 = __x_imp((u"json"))
    json_stringify = __r5.dumps
    __r6 = __x_imp((u"shutil"))
    copyfile = __r6.copyfile
    copytree = __r6.copytree
    subprocess = __x_imp((u"subprocess"))
    SRC_SUFFIX = (u".as")
    SRC_TREE = ({(u"parser"): 2, (u"tools"): ({(u"cas"): 0, (u"esstring"): 1, (u"range"): 1, (u"options"): 
1, (u"__init__"): 1}), (u"ir"): ({(u"ast2ir"): 0, (u"element"): 0, (u"pygen"): 0, (u"symboltree"): 0, 
(u"attribute"): 0, (u"variable"): 0, (u"StringMap"): 0, (u"utils"): 0, (u"compat"): 1, (u"syntax"): 1, 
(u"__init__"): 1}), (u"compile"): 0, (u"bootstrap"): 0})
    __x_at_forEach([DSTPATH, joinPath(DSTPATH, (u"cc1")), joinPath(DSTPATH, (u"cc2")), joinPath(DSTPATH, 
(u"cc3"))], __fB_)
    time_st = time()
    print((u"Stage 1"))
    process((u".."), (u"cc1"))
    print((u"Stage 2"))
    process((u"cc1"), (u"cc2"))
    print((u"Stage 3"))
    process((u"cc2"), (u"cc3"))
    print((u"verifying 1 and 2 (for reference only)..."))
    docompare((u"cc1"), (u"cc2"))
    print((u"verifying..."))
    v = docompare((u"cc2"), (u"cc3"))
    if __x_cb(__x_not(v)):
        print((u"something goes wrong"))
        exit(1)
    else:
        print((u"all correct"))
    # end if
    finalbase = joinPath(DSTPATH, (u"cc3"))
    clean_sh = []
    clean_sh.append((u"find \"") + finalbase + (u"\" -name \"*.json\" -type f -delete"))
    clean_sh.append((u"find \"") + finalbase + (u"\" -name \"*.xml\" -type f -delete"))
    __x_at_forEach(SRC_TREE, __fC_)
    clean_sh.append((u"rm -rf \"") + DSTPATH + (u"\""))
    clean_sh.append((u"rm $0"))
    clean_sh_file = open(joinPath((u"."), (u"cleanandreplace.sh")), (u"wb"))
    try:
        clean_sh_file.write(__x_at_join(clean_sh, (u"\n")).encode((u"utf-8")))
    finally:
        clean_sh_file.close()
    # end try
    print((u"Done. If everything is OK, run cleanandreplace.sh to delete the older version."))
    time_sp = time()
    print((u"Total time consumption: %f s") % (time_sp - time_st))
# program end


__()
