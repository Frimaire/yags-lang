# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, division, generators

__all__ = ()


def __():
    from libyags0 import __x_tup, __x_tupof, __x_lst, __x_errT, __x_eq, __x_ne, __x_typ, __x_cb, __x_not, __x_iof, __x_inc, __x_dec, __x_var, __x_imf, __x_at_take, __x_at_drop, __x_at_forEach, __x_at_map, __x_at_filter, __x_at_flatMap, __x_at_some, __x_at_every, __x_at_find, __x_at_findIndex, __x_at_reduce, __x_at_join, __x_at_bind, __x_at_apply, __x_at_length, __x_at_isEmpty, __x_at_push, __x_at_pop, __x_at_shift, __x_at_unshift, __x_at_slice, __x_at_splice, __x_dcls, __x_dpif, __x_dpsf, __x_prmT, __x_csgT, __x_cpgT, __x_objT, __x_smet, __x_prop, __x_tob, __x_tnb, Infinity, NaN
    __x_imp = __x_imf(__name__)

    # function definitions:

    def dumpIR(ir, path = ((u"unknown-current.xml")), action = (True)):
        if __x_cb(__x_not(action)):
            return
        # end if (line 14)
        dmp = XMLDumper()
        irxml = ir.dump(dmp)
        xmlhead = (u"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
        xmltxt = xmlhead + dmp.toString()
        f = open(path, (u"wb"))
        try:
            f.write(xmltxt.encode((u"utf-8")))
        finally:
            f.close()
        # end try (line 22)
    # end function dumpIR (line 13)

    def dumpAST(ast, path = ((u"unknown-ast.json")), action = (True)):
        if __x_cb(__x_not(action)):
            return
        # end if (line 30)
        asttxt = __x_at_apply(json_stringify, [toDict(ast)], ({(u"indent"): 4}))
        f = open(path, (u"wb"))
        try:
            f.write(asttxt.encode((u"utf-8")))
        finally:
            f.close()
        # end try (line 35)
    # end function dumpAST (line 29)

    def process(srcdir, dstdir, modname, dump = (False), dast = (False), options = (None)):
        srcpath = join(srcdir, modname + (u".as"))
        dstpath = join(dstdir, modname + (u".py"))
        print(srcpath + (u" -> ") + dstpath)
        srcf = open(srcpath, (u"rb"))
        try:
            ascode = srcf.read().decode((u"utf-8"))
        finally:
            srcf.close()
        # end try (line 47)
        dfn = __x_at_slice(dstpath, 0, -3) if __x_cb(__x_eq(__x_at_slice(dstpath, -3), (u".py"))) else dstpath
        ast = __x_at_apply(parse, [ascode], ({(u"options"): ({(u"attachComment"): True, (u"loc"): True, (u"range"): 
True})}))
        dumpAST(ast, dfn + (u"-ast.json"), dast)
        ir = convertASTIR(ast, options)
        try:
            ir.checkAllStructure()
            dumpIR(ir, dfn + (u"-initial.xml"), dump)
            ir.declareVariable()
            ir.checkAllStructure()
            dumpIR(ir, dfn + (u"-declare-variable.xml"), dump)
            ir.checkVariables()
            ir.checkAllStructure()
            dumpIR(ir, dfn + (u"-check-variable.xml"), dump)
            ir.functionalize()
            ir.checkAllStructure()
            dumpIR(ir, dfn + (u"-functionalize.xml"), dump)
            ir.simplifyExpressions()
            ir.checkAllStructure()
            dumpIR(ir, dfn + (u"-simplify-expressions.xml"), dump)
        finally:
            dumpIR(ir, dfn + (u"-current.xml"), dump)
        # end try (line 57)
        gen = PyGenerator()
        ir.generatePython(gen)
        pytxt = gen.finalize()
        pyf = open(dstpath, (u"wb"))
        try:
            pyf.write(pytxt.encode((u"utf-8")))
        finally:
            pyf.close()
        # end try (line 79)
    # end function process (line 42)

    def copypy(srcdir, dstdir, modname):
        srcpath = join(srcdir, modname + (u".py"))
        dstpath = join(dstdir, modname + (u".py"))
        print(srcpath + (u" -> ") + dstpath)
        copyfile(srcpath, dstpath)
    # end function copypy (line 86)

    def readall(path):
        fp = open(path, (u"r"))
        try:
            return fp.read()
        finally:
            fp.close
        # end try (line 95)
    # end function readall (line 93)

    def __f6_(fn, k):
        process(srcirdir, dstirdir, fn, DUMP_IR, DUMP_AST)
    # end function <anonymous> (__f6_) (line 102)

    def __f7_(fn, k):
        copypy(srcirdir, dstirdir, fn)
    # end function <anonymous> (__f7_) (line 106)

    def __f8_(fn, k):
        process(srcirdir, dstirdir, fn, DUMP_IR, DUMP_AST)
    # end function <anonymous> (__f8_) (line 110)

    def __f9_(fn, k):
        copypy(srcirdir, dstirdir, fn)
    # end function <anonymous> (__f9_) (line 114)

    def __fA_(fn, k):
        process(srcirdir, dstirdir, fn, DUMP_IR, DUMP_AST)
    # end function <anonymous> (__fA_) (line 118)

    def __fB_(fn, k):
        copypy(srcirdir, dstirdir, fn)
    # end function <anonymous> (__fB_) (line 122)

    def __fC_(fn, k):
        distpath = join(dstirdir2, fn + (u".py"))
        dstpath = join(dstirdir3, fn + (u".py"))
        dist = readall(distpath)
        dst = readall(dstpath)
        f = __x_eq(dist, dst)
        __u_v.val = __x_cb(__u_v.val) and f
        print(fn + (u" ") + ((u"verified") if __x_cb(f) else (u"differs")))
    # end function <anonymous> (__fC_) (line 126)

    # class definitions:
    __u_v = __x_var()

    SRCPATH = (u"..")
    DUMP_AST = False
    DUMP_IR = False
    __r0 = __x_imp((u"os"))
    mkdir = __r0.mkdir
    __r1 = __x_imp((u"os.path"))
    join = __r1.join
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
    __r7 = __x_imp((u"parser.esprima"))
    parse = __r7.parse
    toDict = __r7.toDict
    __r8 = __x_imp((u"ir.ast2ir"))
    convertASTIR = __r8.convertASTIR
    __r9 = __x_imp((u"ir.utils"))
    XMLDumper = __r9.XMLDumper
    __rA = __x_imp((u"ir.pygen"))
    PyGenerator = __rA.PyGenerator
    __rB = __x_imp((u"ir.StringMap"))
    StringMap = __rB.StringMap
    time_st = time()
    dstscriptdir = join((u"."), (u"scripts-n"))
    try:
        mkdir(dstscriptdir)
    except __x_errT as errsc:
        print((u"Cannot create the directory for compiler scripts (scripts-n). If the directory already exists, pleas\
e delete it manually at first."))
        exit()
    # end try (line 173)
    src_list = [(u"ast2ir"), (u"element"), (u"pygen"), (u"symboltree"), (u"identifier"), (u"StringMap"), 
(u"utils")]
    py_list = [(u"compat"), (u"syntax"), (u"__init__")]
    print((u"Stage 1"))
    srcirdir = join(SRCPATH, (u"ir"))
    dstirdir = join((u"."), (u"ir1"))
    try:
        mkdir(dstirdir)
    except __x_errT as err1:
        print((u"Cannot create the directory for stage 1 ir. If the directory already exists, please delete it manual\
ly at first."))
        exit()
    # end try (line 186)
    __x_at_forEach(src_list, __f6_)
    __x_at_forEach(py_list, __f7_)
    print((u"Stage 2"))
    __rC = __x_imp((u"ir1.ast2ir"))
    convertASTIR = __rC.convertASTIR
    __rD = __x_imp((u"ir1.utils"))
    XMLDumper = __rD.XMLDumper
    __rE = __x_imp((u"ir1.pygen"))
    PyGenerator = __rE.PyGenerator
    __rF = __x_imp((u"ir1.StringMap"))
    StringMap = __rF.StringMap
    dstirdir = join((u"."), (u"ir2"))
    dstirdir2 = dstirdir
    try:
        mkdir(dstirdir)
    except __x_errT as err2:
        print((u"Cannot create the directory for stage 2 ir. If the directory already exists, please delete it manual\
ly at first."))
        exit()
    # end try (line 206)
    __x_at_forEach(src_list, __f8_)
    __x_at_forEach(py_list, __f9_)
    print((u"Stage 3"))
    __rG = __x_imp((u"ir2.ast2ir"))
    convertASTIR = __rG.convertASTIR
    __rH = __x_imp((u"ir2.utils"))
    XMLDumper = __rH.XMLDumper
    __rI = __x_imp((u"ir2.pygen"))
    PyGenerator = __rI.PyGenerator
    __rJ = __x_imp((u"ir2.StringMap"))
    StringMap = __rJ.StringMap
    dstirdir = join((u"."), (u"ir3"))
    dstirdir3 = dstirdir
    try:
        mkdir(dstirdir)
    except __x_errT as err3:
        print((u"Cannot create the directory for stage 3 ir. If the directory already exists, please delete it manual\
ly at first."))
        exit()
    # end try (line 226)
    __x_at_forEach(src_list, __fA_)
    __x_at_forEach(py_list, __fB_)
    print((u"verifying..."))
    __u_v.val = True
    __x_at_forEach(src_list, __fC_)
    print((u"all correct") if __x_cb(__u_v.val) else (u"something goes wrong"))
    process(SRCPATH, dstscriptdir, (u"compile"), DUMP_IR, DUMP_AST)
    process(SRCPATH, dstscriptdir, (u"bootstrap"), DUMP_IR, DUMP_AST)
    clean_sh = (u"rm -rf parser/__pycache__\nrm -rf ir\nrm -rf ir1\n\
rm -rf ir2\nrm ir3/*.xml\nrm ir3/*.json\nmv ir3 ir\n\
mv scripts-n/compile.py ./compile.py\nmv scripts-n/bootstrap.py ./bootstrap.py\n\
rm -rf scripts-n\nrm $0")
    clean_sh_file = open(join((u"."), (u"cleanandreplace.sh")), (u"wb"))
    try:
        clean_sh_file.write(clean_sh.encode((u"utf-8")))
    finally:
        clean_sh_file.close()
    # end try (line 246)
    print((u"Done. If everything is OK, run cleanandreplace.sh to delete the older version."))
    time_sp = time()
    print((u"Time cost: %f s") % (time_sp - time_st))
# program end


__()
