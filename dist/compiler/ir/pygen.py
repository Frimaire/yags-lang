# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, division, generators

__all__ = ("LineNumber", "LineWriter", "PyGenerator")


def __():
    from libyags0 import __x_tup, __x_tupof, __x_lst, __x_errT, __x_eq, __x_ne, __x_typ, __x_cb, __x_not, __x_iof, __x_inc, __x_dec, __x_var, __x_imf, __x_at_take, __x_at_drop, __x_at_forEach, __x_at_map, __x_at_filter, __x_at_flatMap, __x_at_some, __x_at_every, __x_at_find, __x_at_findIndex, __x_at_reduce, __x_at_join, __x_at_bind, __x_at_apply, __x_at_length, __x_at_isEmpty, __x_at_push, __x_at_pop, __x_at_shift, __x_at_unshift, __x_at_slice, __x_at_splice, __x_dcls, __x_dpif, __x_dpsf, __x_prmT, __x_csgT, __x_cpgT, __x_objT, __x_smet, __x_prop, __x_tob, __x_tnb, Infinity, NaN
    __x_imp = __x_imf(__name__)
    global LineNumber, LineWriter, PyGenerator

    # function definitions:

    def makeTabs(n):
        ts = (u"    ")
        s = (u"")
        while True:
            __r0 = __x_cb
            __r1 = n
            n = __x_dec(__r1)
            if not __r0(__r1 > 0):
                break
            # end if (line 21)
            s = s + ts
        # end while (line 17)
        return s
    # end function makeTabs (line 14)

    # class definitions:

    def __c_LineNumber():
        def __m_LineNumber(this):
            __csu(this)
        # end function __m_LineNumber (line 32)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 36)

        def __csu(this, *argv):
            # initialize properties
            this.lineNumber = -1
            this.used = False
            this.prev = False
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 42)

        __clsT = __x_dcls("LineNumber", __x_objT, {"__slots__": (), "__init__": __csi}, {"__slots__": ("lineNumber", 
"prev", "used"), "__init__": __m_LineNumber})
        return __clsT
    # end class factory LineNumber, __c_LineNumber (line 31)

    def __c_LineWriter():
        def __m_write(this, source, linebreak = (False)):
            if __x_cb(__x_eq(linebreak, False)):
                breakHere = False
                allowBreak = False
                contchar = None
            elif __x_cb(__x_eq(linebreak, True)):
                breakHere = True
                allowBreak = False
                contchar = None
            elif __x_cb(__x_eq(__x_typ(linebreak), (u"string"))):
                breakHere = False
                allowBreak = True
                contchar = linebreak
            else:
                raise InternalError((u"Illegal linebreak type"))
            # end if (line 58)
            this.spans.push(LineSpan(source, breakHere, allowBreak, contchar))
        # end function __m_write (line 57)

        def __m_finalize(this, genctx):
            def __f9_(e, k, a):
                __u_s.val = __u_s.val + e.source
                __u_l.val = __u_l.val + e.length
                lb = False
                if __x_cb(e.breakHere):
                    lb = True
                elif __x_cb(__x_cb(__x_cb(e.allowBreak) and __u_l.val > LINE_LENGTH) and __x_ne(k, a.length - 1)):
                    __u_s.val = __u_s.val + e.contchar
                    lb = True
                # end if (line 81)
                if __x_cb(__x_cb(lb) and __x_ne(k, a.length - 1)):
                    genctx.writeln(__u_s.val) if __x_cb(__u_first.val) else genctx.write(__u_s.val)
                    __u_first.val = False
                    __u_s.val = (u"")
                    __u_l.val = 0
                # end if (line 87)
            # end function <anonymous> (__f9_) (line 77)

            __u_first = __x_var()
            __u_l = __x_var()
            __u_s = __x_var()
            if __x_cb(this.spans.length <= 0):
                raise InternalError((u"empty line"))
            # end if (line 98)
            __u_s.val = (u"")
            __u_l.val = 0
            __u_first.val = True
            this.spans.forEach(__f9_)
            if __x_cb(__u_l.val > 0):
                genctx.writeln(__u_s.val) if __x_cb(__u_first.val) else genctx.write(__u_s.val)
            # end if (line 105)
        # end function __m_finalize (line 76)

        def __m_LineWriter(this):
            __csu(this)
        # end function __m_LineWriter (line 110)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 114)

        def __csu(this, *argv):
            # initialize properties
            this.spans = ArrayList()
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 120)

        __clsT = __x_dcls("LineWriter", __x_objT, {"__slots__": (), "__init__": __csi}, {"__slots__": ("spans",), 
"finalize": __m_finalize, "write": __m_write, "__init__": __m_LineWriter})
        return __clsT
    # end class factory LineWriter, __c_LineWriter (line 56)

    def __c_LineSpan():
        def __m_LineSpan(this, source, breakHere, allowBreak, contchar):
            __csu(this)
            this.source = source
            this.length = StrTool.strlen(source)
            this.breakHere = breakHere
            this.allowBreak = allowBreak
            this.contchar = contchar
        # end function __m_LineSpan (line 133)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 142)

        def __csu(this, *argv):
            # initialize properties
            this.breakHere = False
            this.allowBreak = False
            this.contchar = (u"\\")
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 148)

        __clsT = __x_dcls("LineSpan", __x_objT, {"__slots__": (), "__init__": __csi}, {"__slots__": ("allowBreak", 
"breakHere", "contchar", "length", "source"), "__init__": __m_LineSpan})
        return __clsT
    # end class factory LineSpan, __c_LineSpan (line 132)

    def __c_PyGenerator():
        def __m_tab(this):
            __r0 = this
            __r1 = __r0.tabs
            __r0.tabs = __x_inc(__r1)
            this.outputed = False
        # end function __m_tab (line 163)

        def __m_TAB(this):
            if __x_cb(__x_not(this.outputed)):
                this.writeln((u"pass"))
            # end if (line 171)
            __r0 = this
            __r1 = __r0.tabs
            __r0.tabs = __x_dec(__r1)
            if __x_cb(this.tabs < 0):
                raise InternalError((u"set tabs to negative"))
            # end if (line 177)
            this.outputed = True
        # end function __m_TAB (line 170)

        def __m_appendComment(this, s):
            def __fL_(c, k, a):
                if __x_cb(__x_eq(c, (u"\n"))):
                    comment((u"%s"), __u_sl.val)
                    __u_sl.val = (u"")
                    return
                # end if (line 185)
                __u_sl.val = __u_sl.val + c
            # end function <anonymous> (__fL_) (line 184)

            __u_sl = __x_var()
            __u_sl.val = (u"")
            comment = this.comment
            ArrayList(s).forEach(__fL_)
            if __x_cb(__x_ne(__u_sl.val, (u""))):
                comment((u"%s"), __u_sl.val)
            # end if (line 197)
        # end function __m_appendComment (line 183)

        def __m_comment(this, format, *argv):
            this.lines.push(Comment(this.tabs, format, ArrayList(argv)))
            this.outputed = True
        # end function __m_comment (line 202)

        def __m_logLineNumber(this, o, prev = (False)):
            if __x_cb(o.used):
                raise InternalError((u"used line number anchor!"))
            # end if (line 208)
            __r0 = o
            __r0.used = True
            __r1 = o
            __r1.prev = prev
            this.lines.push(o)
        # end function __m_logLineNumber (line 207)

        def __m_writeln(this, line):
            this.lines.push(Code(this.tabs, line))
            this.outputed = True
        # end function __m_writeln (line 218)

        def __m_write(this, line):
            this.lines.push(Code(0, line))
        # end function __m_write (line 223)

        def __m_blank(this):
            if __x_cb(this.outputed):
                this.lines.push(None)
            # end if (line 228)
        # end function __m_blank (line 227)

        def __m_finalize(this):
            def __fS_(line, k, a):
                if __x_cb(__x_iof(line, LineNumber)):
                    __r0 = line
                    __r0.lineNumber = __u_ln.val
                elif __x_cb(__x_cb(__x_eq(line, None)) and allowBlank):
                    __r1 = __u_ln.val
                    __u_ln.val = __x_inc(__r1)
                else:
                    __r2 = __u_ln.val
                    __u_ln.val = __x_inc(__r2)
                # end if (line 235)
            # end function <anonymous> (__fS_) (line 234)

            def __fT_(line, k, a):
                if __x_cb(__x_iof(line, LineNumber)):
                    return
                # end if (line 248)
                if __x_cb(__x_eq(line, None)):
                    if __x_cb(allowBlank):
                        __u_s.val = __u_s.val + (u"\n")
                    # end if (line 252)
                    return
                # end if (line 251)
                __u_s.val = __u_s.val + line.finalize()
            # end function <anonymous> (__fT_) (line 247)

            __u_ln = __x_var()
            __u_s = __x_var()
            __u_s.val = (u"")
            __u_ln.val = 0
            allowBlank = this.allowBlank
            this.lines.forEach(__fS_)
            this.lines.forEach(__fT_)
            return __u_s.val
        # end function __m_finalize (line 233)

        def __m_PyGenerator(this):
            __csu(this)
        # end function __m_PyGenerator (line 270)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 274)

        def __csu(this, *argv):
            # initialize properties
            this.lines = ArrayList()
            this.allowComment = True
            this.allowBlank = True
            this.tabs = 0
            this.outputed = False
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 280)

        __clsT = __x_dcls("PyGenerator", __x_objT, {"__slots__": (), "__init__": __csi}, {"__slots__": ("allowBlank", 
"allowComment", "lines", "outputed", "tabs"), "TAB": __m_TAB, "appendComment": __m_appendComment, "blank": __m_blank, 
"comment": __m_comment, "finalize": __m_finalize, "logLineNumber": __m_logLineNumber, "tab": __m_tab, 
"write": __m_write, "writeln": __m_writeln, "__init__": __m_PyGenerator})
        return __clsT
    # end class factory PyGenerator, __c_PyGenerator (line 162)

    def __c_Code():
        def __m_finalize(this):
            return makeTabs(this.tabs) + this.source + (u"\n")
        # end function __m_finalize (line 299)

        def __m_Code(this, tabs, source):
            __csu(this)
            this.tabs = tabs
            this.source = source
        # end function __m_Code (line 303)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 309)

        def __csu(this, *argv):
            # initialize properties
            this.tabs = 0
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 315)

        __clsT = __x_dcls("Code", __x_objT, {"__slots__": (), "__init__": __csi}, {"__slots__": ("source", "tabs"), 
"finalize": __m_finalize, "__init__": __m_Code})
        return __clsT
    # end class factory Code, __c_Code (line 298)

    def __c_Comment():
        def __m_finalize(this):
            def __f18_(c, k, a):
                if __x_cb(__x_not(__u_p.val)):
                    if __x_cb(__x_eq(c, (u"%"))):
                        __u_p.val = True
                    else:
                        __u_s.val = __u_s.val + c
                    # end if (line 331)
                    return
                # end if (line 330)
                if __x_cb(__x_eq(c, (u"%"))):
                    __u_s.val = __u_s.val + (u"%")
                elif __x_cb(__x_eq(c, (u"l"))):
                    __r0 = argv.get
                    __r1 = __u_argc.val
                    __u_argc.val = __x_inc(__r1)
                    e = __r0(__r1)
                    if __x_cb(__x_not(__x_cb(e.lineNumber > 0) or (__x_cb(__x_eq(e.lineNumber, 0)) and __x_not(e.prev)))):
                        raise InternalError((u"uninitialized line number anchor"), e)
                    # end if (line 345)
                    __u_s.val = __u_s.val + StrTool.str(e.lineNumber + (0 if __x_cb(e.prev) else 1))
                elif __x_cb(__x_eq(c, (u"s"))):
                    __r2 = __u_s.val
                    __r3 = StrTool.str
                    __r4 = argv.get
                    __r5 = __u_argc.val
                    __u_argc.val = __x_inc(__r5)
                    __u_s.val = __r2 + __r3(__r4(__r5))
                else:
                    raise InternalError((u"unknown comment formatter ") + c)
                # end if (line 338)
                __u_p.val = False
            # end function <anonymous> (__f18_) (line 329)

            __u_argc = __x_var()
            __u_p = __x_var()
            __u_s = __x_var()
            __u_s.val = makeTabs(this.tabs) + (u"# ")
            __u_p.val = False
            __u_argc.val = 0
            argv = this.argv
            ArrayList(this.source).forEach(__f18_)
            if __x_cb(__u_p.val):
                raise InternalError((u"unprocessed comment formatter"))
            # end if (line 370)
            return __u_s.val + (u"\n")
        # end function __m_finalize (line 328)

        def __m_Comment(this, tabs, source, argv):
            __csu(this)
            this.tabs = tabs
            this.source = source
            this.argv = argv
        # end function __m_Comment (line 376)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 383)

        def __csu(this, *argv):
            # initialize properties
            this.tabs = 0
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 389)

        __clsT = __x_dcls("Comment", __x_objT, {"__slots__": (), "__init__": __csi}, {"__slots__": ("argv", "source", 
"tabs"), "finalize": __m_finalize, "__init__": __m_Comment})
        return __clsT
    # end class factory Comment, __c_Comment (line 327)

    __r0 = __x_imp((u".compat"))
    ArrayList = __r0.ArrayList
    StrTool = __r0.StrTool
    __r1 = __x_imp((u".utils"))
    CompileError = __r1.CompileError
    ElementPattern = __r1.ElementPattern
    Range = __r1.Range
    ConflictError = __r1.ConflictError
    InternalError = __r1.InternalError
    XMLDumper = __r1.XMLDumper
    LineNumber = __c_LineNumber()
    LineWriter = __c_LineWriter()
    LINE_LENGTH = 100
    LineSpan = __c_LineSpan()
    PyGenerator = __c_PyGenerator()
    Code = __c_Code()
    Comment = __c_Comment()
# program end


__()
