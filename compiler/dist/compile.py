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

    def process(srcpath, dstpath, dump = (False), dast = (False), options = (None)):
        srcf = open(srcpath, (u"rb"))
        try:
            ascode = srcf.read().decode((u"utf-8"))
        finally:
            srcf.close()
        # end try (line 44)
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
        # end try (line 54)
        gen = PyGenerator()
        ir.generatePython(gen)
        pytxt = gen.finalize()
        pyf = open(dstpath, (u"wb"))
        try:
            pyf.write(pytxt.encode((u"utf-8")))
        finally:
            pyf.close()
        # end try (line 76)
    # end function process (line 42)

    def aarg(argv, o):
        __x_at_apply(argp.add_argument, argv, o)
    # end function aarg (line 83)

    # class definitions:

    __r0 = __x_imp((u"os.path"))
    join = __r0.join
    dirname = __r0.dirname
    basename = __r0.basename
    isdir = __r0.isdir
    normpath = __r0.normpath
    __r1 = __x_imp((u"sys"))
    pyver = __r1.version_info
    __r2 = __x_imp((u"argparse"))
    ArgumentParser = __r2.ArgumentParser
    __r3 = __x_imp((u"json"))
    json_stringify = __r3.dumps
    __r4 = __x_imp((u"parser.esprima"))
    parse = __r4.parse
    toDict = __r4.toDict
    __r5 = __x_imp((u"ir.ast2ir"))
    convertASTIR = __r5.convertASTIR
    __r6 = __x_imp((u"ir.utils"))
    XMLDumper = __r6.XMLDumper
    __r7 = __x_imp((u"ir.pygen"))
    PyGenerator = __r7.PyGenerator
    __r8 = __x_imp((u"ir.StringMap"))
    StringMap = __r8.StringMap
    version = (u"0.1")
    argp = ArgumentParser((u"yags"), None, (u"Compile YAGS to Python code"))
    aarg([(u"-v"), (u"--version")], ({(u"action"): (u"version"), (u"version"): ((u"YAGS compiler %s (on Python %d.%d)")
 % tuple([version, pyver.major, pyver.minor]))}))
    aarg([(u"-d"), (u"--dump-ir")], ({(u"action"): (u"store_true"), (u"dest"): (u"allowDumpIR"), (u"help"): 
(u"Dump the intermediate representation as XML into the output directory.")}))
    aarg([(u"-a"), (u"--dump-ast")], ({(u"action"): (u"store_true"), (u"dest"): (u"allowDumpAST"), (u"help"): 
(u"Dump the syntax tree as JSON into the output directory.")}))
    aarg([(u"-o"), (u"--output")], ({(u"action"): (u"store"), (u"dest"): (u"dstpath"), (u"metavar"): (u"OUTPUT_FILE"), 
(u"help"): (u"Specify the path of output file. If this is not specified, the same directory as the input will be u\
sed as the output directory.")}))
    aarg([(u"input")], ({(u"action"): (u"store"), (u"metavar"): (u"INPUT_FILE"), (u"help"): (u"Specify the path of input file.")}))
    aarg([(u"--enable-implicit-bool")], ({(u"action"): (u"store_true"), (u"dest"): (u"implBoolConv"), (u"help"): 
(u"Enable experimental implicit boolean conversion.")}))
    __r9 = argp.parse_args()
    allowDumpIR = __r9.allowDumpIR
    allowDumpAST = __r9.allowDumpAST
    dstpath = __r9.dstpath
    implBoolConv = __r9.implBoolConv
    srcpath = __r9.input
    srcpath = normpath(srcpath)
    if __x_cb(__x_eq(dstpath, None)):
        fn = basename(srcpath)
        fn = (__x_at_slice(fn, 0, -5) if __x_cb(__x_eq(__x_at_slice(fn, -5), (u".yags"))) else (__x_at_slice(fn, 
0, -3) if __x_cb(__x_eq(__x_at_slice(fn, -3), (u".as"))) else fn)) + (u".py")
        dstpath = join(dirname(srcpath), fn)
    # end if (line 133)
    process(srcpath, dstpath, allowDumpIR, allowDumpAST, StringMap([[(u"enableImplicitBooleanConversion"), 
implBoolConv]]))
# program end


__()
