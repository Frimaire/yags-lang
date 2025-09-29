# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, division, generators

__all__ = ()


def __():
    from libyags0 import __x_tup, __x_tupof, __x_lst, __x_errT, __x_eq, __x_ne, __x_typ, __x_cb, __x_not, __x_iof, __x_inc, __x_dec, __x_var, __x_imf, __x_at_take, __x_at_drop, __x_at_forEach, __x_at_map, __x_at_filter, __x_at_flatMap, __x_at_some, __x_at_every, __x_at_find, __x_at_findIndex, __x_at_reduce, __x_at_join, __x_at_bind, __x_at_apply, __x_at_length, __x_at_isEmpty, __x_at_push, __x_at_pop, __x_at_shift, __x_at_unshift, __x_at_slice, __x_at_splice, __x_at_has, __x_dcls, __x_dpif, __x_dpsf, __x_prmT, __x_csgT, __x_cpgT, __x_objT, __x_smet, __x_prop, __x_tob, __x_tnb, Infinity, NaN
    __x_imp = __x_imf(__name__)

    # function definitions:

    def dumpIR(ir, path = ((u"unknown-current.xml")), action = (True)):
        if __x_cb(__x_not(action)):
            return
        # end if
        dmp = XMLDumper()
        irxml = ir.dump(dmp)
        xmlhead = (u"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
        xmltxt = xmlhead + dmp.toString()
        f = open(path, (u"wb"))
        try:
            f.write(xmltxt.encode((u"utf-8")))
        finally:
            f.close()
        # end try
    # end function dumpIR

    def dumpAST(ast, path = ((u"unknown-ast.json")), action = (True)):
        if __x_cb(__x_not(action)):
            return
        # end if
        asttxt = __x_at_apply(json_stringify, [toDict(ast)], ({(u"indent"): 4}))
        f = open(path, (u"wb"))
        try:
            f.write(asttxt.encode((u"utf-8")))
        finally:
            f.close()
        # end try
    # end function dumpAST

    def process(srcpath, dstpath, dump = (False), dast = (False)):
        initAlert(srcpath, None)
        srcf = None
        try:
            srcf = open(srcpath, (u"rb"))
            ascode = srcf.read().decode((u"utf-8"))
        except __x_errT as iferr:
            error((u"Can not open the input file: %s"), str(iferr))
        finally:
            if __x_cb(__x_ne(srcf, None)):
                srcf.close()
            # end if
        # end try
        initAlert(srcpath, ascode)
        dfn = __x_at_slice(dstpath, 0, -3) if __x_cb(__x_eq(__x_at_slice(dstpath, -3), (u".py"))) else dstpath
        __u_timeReaded.val = time()
        ast = __x_at_apply(parse, [ascode], ({(u"options"): ({(u"attachComment"): True, (u"loc"): True, (u"range"): 
True})}))
        dumpAST(ast, dfn + (u"-ast.json"), dast)
        __u_timeParse.val = time()
        ir = convertASTIR(ast)
        __u_timeConvIR.val = time()
        try:
            ir.checkAllStructure()
            dumpIR(ir, dfn + (u"-initial.xml"), dump)
            ir.declareVariable()
            ir.checkAllStructure()
            dumpIR(ir, dfn + (u"-declare-variable.xml"), dump)
            __u_timeDecl.val = time()
            ir.checkVariables()
            ir.checkAllStructure()
            dumpIR(ir, dfn + (u"-check-variable.xml"), dump)
            __u_timeCheck.val = time()
            ir.functionalize()
            ir.checkAllStructure()
            dumpIR(ir, dfn + (u"-functionalize.xml"), dump)
            __u_timeFunc.val = time()
            ir.simplifyExpressions()
            ir.checkAllStructure()
            dumpIR(ir, dfn + (u"-simplify-expressions.xml"), dump)
            __u_timeSimp.val = time()
        finally:
            dumpIR(ir, dfn + (u"-current.xml"), dump)
        # end try
        gen = PyGenerator()
        ir.generatePython(gen)
        pytxt = gen.finalize()
        pyf = None
        try:
            pyf = open(dstpath, (u"wb"))
            pyf.write(pytxt.encode((u"utf-8")))
        except __x_errT as oferr:
            error((u"Can not open the output file: %s"), str(oferr))
        finally:
            if __x_cb(__x_ne(pyf, None)):
                pyf.close()
            # end if
        # end try
    # end function process

    def aarg(argv, o):
        __x_at_apply(argp.add_argument, argv, o)
    # end function aarg

    # class definitions:
    __u_timeCheck = __x_var()
    __u_timeConvIR = __x_var()
    __u_timeDecl = __x_var()
    __u_timeFunc = __x_var()
    __u_timeParse = __x_var()
    __u_timeReaded = __x_var()
    __u_timeSimp = __x_var()

    __r0 = __x_imp((u"time"))
    time = __r0.time
    timeStart = time()
    __r1 = __x_imp((u"os.path"))
    join = __r1.join
    dirname = __r1.dirname
    basename = __r1.basename
    isdir = __r1.isdir
    normpath = __r1.normpath
    __r2 = __x_imp((u"sys"))
    pyver = __r2.version_info
    __r3 = __x_imp((u"argparse"))
    ArgumentParser = __r3.ArgumentParser
    __r4 = __x_imp((u"json"))
    json_stringify = __r4.dumps
    __r5 = __x_imp((u"parser.esprima"))
    parse = __r5.parse
    toDict = __r5.toDict
    __r6 = __x_imp((u"ir.ast2ir"))
    convertASTIR = __r6.convertASTIR
    __r7 = __x_imp((u"ir.utils"))
    XMLDumper = __r7.XMLDumper
    __r8 = __x_imp((u"ir.pygen"))
    PyGenerator = __r8.PyGenerator
    __r9 = __x_imp((u"ir.StringMap"))
    StringMap = __r9.StringMap
    __rA = __x_imp((u"tools.cas"))
    CompileError = __rA.CompileError
    initAlert = __rA.init
    error = __rA.error
    note = __rA.note
    __rB = __x_imp((u"tools.options"))
    options = __rB.options
    timeLoaded = time()
    version = (u"0.2")
    argp = ArgumentParser((u"yags"), None, (u"Compile YAGS to Python code"))
    aarg([(u"-v"), (u"--version")], ({(u"action"): (u"version"), (u"version"): ((u"YAGS compiler %s (on Python %d.%d)")
 % tuple([version, pyver.major, pyver.minor]))}))
    aarg([(u"-o"), (u"--output")], ({(u"action"): (u"store"), (u"dest"): (u"dstpath"), (u"metavar"): (u"OUTPUT_FILE"), 
(u"help"): (u"Specify the path of output file. If this is not specified, the same directory as the input will be u\
sed as the output directory.")}))
    aarg([(u"input")], ({(u"action"): (u"store"), (u"metavar"): (u"INPUT_FILE"), (u"help"): (u"Specify the path of input file.")}))
    aarg([(u"--enable-implicit-bool")], ({(u"action"): (u"store_true"), (u"dest"): (u"enableImplicitBooleanConversion"), 
(u"help"): (u"Enable experimental implicit boolean conversion.")}))
    aarg([(u"--enable-tuple-subscription")], ({(u"action"): (u"store_true"), (u"dest"): (u"enableTupleSubscription"), 
(u"help"): (u"Enable experimental tuple subscription. That is, allow comma-separated expressions in the object[exp\
ressions] syntax, which will be converted to a tuple. This feature is used to facilitate the access \
of some multidimensional arraies such as numpy.ndarray.")}))
    aarg([(u"--dump-ir")], ({(u"action"): (u"store_true"), (u"dest"): (u"allowDumpIR"), (u"help"): (u"Dump the intermediate representation as XML into the output directory.")}))
    aarg([(u"--dump-ast")], ({(u"action"): (u"store_true"), (u"dest"): (u"allowDumpAST"), (u"help"): (u"Dump the syntax tree as JSON into the output directory.")}))
    aarg([(u"--trace-profile")], ({(u"action"): (u"store_true"), (u"dest"): (u"traceProfile"), (u"help"): 
(u"Show the time used for each stage.")}))
    __rC = argp.parse_args()
    allowDumpIR = __rC.allowDumpIR
    allowDumpAST = __rC.allowDumpAST
    dstpath = __rC.dstpath
    srcpath = __rC.input
    enableImplicitBooleanConversion = __rC.enableImplicitBooleanConversion
    enableTupleSubscription = __rC.enableTupleSubscription
    traceProfile = __rC.traceProfile
    timeArgParsed = time()
    __rD = options
    __rD.enableImplicitBooleanConversion = enableImplicitBooleanConversion
    __rE = options
    __rE.enableTupleSubscription = enableTupleSubscription
    srcpath = normpath(srcpath)
    if __x_cb(__x_eq(dstpath, None)):
        fn = basename(srcpath)
        fn = (__x_at_slice(fn, 0, -5) if __x_cb(__x_eq(__x_at_slice(fn, -5), (u".yags"))) else (__x_at_slice(fn, 
0, -3) if __x_cb(__x_eq(__x_at_slice(fn, -3), (u".as"))) else fn)) + (u".py")
        dstpath = join(dirname(srcpath), fn)
    # end if
    try:
        process(srcpath, dstpath, allowDumpIR, allowDumpAST)
    except __x_errT as ce:
        if __x_cb(__x_iof(ce, CompileError)):
            print((u"compilation terminated"))
            exit(1)
        else:
            raise ce
        # end if
    # end try
    timeFin = time()
    if __x_cb(traceProfile):
        note((u"Time used:"))
        note((u"Load: %.3f s"), timeLoaded - timeStart)
        note((u"Get options: %.3f s"), timeArgParsed - timeLoaded)
        note((u"Read input: %.3f s"), __u_timeReaded.val - timeArgParsed)
        note((u"Parse: %.3f s"), __u_timeParse.val - __u_timeReaded.val)
        note((u"Convert to IR: %.3f s"), __u_timeConvIR.val - __u_timeParse.val)
        note((u"Declare variables: %.3f s"), __u_timeDecl.val - __u_timeConvIR.val)
        note((u"Check variables: %.3f s"), __u_timeCheck.val - __u_timeDecl.val)
        note((u"Functionalize: %.3f s"), __u_timeFunc.val - __u_timeCheck.val)
        note((u"Simplify: %.3f s"), __u_timeSimp.val - __u_timeFunc.val)
        note((u"Generate Python: %.3f s"), timeFin - __u_timeSimp.val)
        note((u"Total: %.3f s"), timeFin - timeStart)
    # end if
# program end


__()
