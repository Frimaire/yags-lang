# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, division, generators

__all__ = ("CompileError", "ConflictError", "ElementPattern", "InternalError", "Range", "XMLDumper")


def __():
    from libyags0 import __x_tup, __x_tupof, __x_lst, __x_errT, __x_eq, __x_ne, __x_typ, __x_cb, __x_not, __x_iof, __x_inc, __x_dec, __x_var, __x_imf, __x_at_take, __x_at_drop, __x_at_forEach, __x_at_map, __x_at_filter, __x_at_flatMap, __x_at_some, __x_at_every, __x_at_find, __x_at_findIndex, __x_at_reduce, __x_at_join, __x_at_bind, __x_at_apply, __x_at_length, __x_at_isEmpty, __x_at_push, __x_at_pop, __x_at_shift, __x_at_unshift, __x_at_slice, __x_at_splice, __x_dcls, __x_dpif, __x_dpsf, __x_prmT, __x_csgT, __x_cpgT, __x_objT, __x_smet, __x_prop, __x_tob, __x_tnb, Infinity, NaN
    __x_imp = __x_imf(__name__)
    global CompileError, ConflictError, ElementPattern, InternalError, Range, XMLDumper

    # function definitions:

    # class definitions:

    def __c_InternalError(__cexT):
        def __m_InternalError(this, message, *extras):
            __csu(this, message)
            this.extraInfo = extras
        # end function __m_InternalError (line 17)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 22)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 28)

        __clsT = __x_dcls("InternalError", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": ("extraInfo",), 
"__init__": __m_InternalError})
        return __clsT
    # end class factory InternalError, __c_InternalError (line 16)

    def __c_CompileError(__cexT):
        def __m_CompileError(this, format, range = (None), *rest):
            info = printf(format, rest)
            __csu(this, info)
            this.range = range
            this.info = info
        # end function __m_CompileError (line 40)

        def __m_toString(this):
            if __x_cb(__x_eq(this.range, None)):
                return (u"Line <unknown>: ") + this.info
            # end if (line 48)
            return printf((u"Line %d: %s"), [this.range.startLine, this.info])
        # end function __m_toString (line 47)

        def __m_____str____(this):
            return this.toString()
        # end function __str__(__m_____str____) (line 54)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 58)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 64)

        __clsT = __x_dcls("CompileError", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": ("info", 
"range"), "__str__": __m_____str____, "toString": __m_toString, "__init__": __m_CompileError})
        return __clsT
    # end class factory CompileError, __c_CompileError (line 39)

    def __c_ConflictError(__cexT):
        def __m_ConflictError(this, format, rangeOccur = (None), rangeOrigin = (None), *rest):
            __csu(this, (u"%s"), rangeOccur, printf(format, rest))
            this.rangeOrigin = rangeOrigin
        # end function __m_ConflictError (line 76)

        def __m_toString(this):
            s = (super(__clsT, this)).toString()
            if __x_cb(__x_ne(this.rangeOrigin, None)):
                s = s + printf((u" (originally defined in line %d)"), [this.rangeOrigin.startLine])
            # end if (line 83)
            return s
        # end function __m_toString (line 81)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 89)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 95)

        __clsT = __x_dcls("ConflictError", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": ("rangeOrigin",), 
"toString": __m_toString, "__init__": __m_ConflictError})
        return __clsT
    # end class factory ConflictError, __c_ConflictError (line 75)

    def __c_ElementPattern():
        def __m_reset(this):
            __cpm[this, "ncnt"] = 0
        # end function __m_reset (line 107)

        def __m_meet(this, e, s):
            if __x_cb(__x_cb(__cpm[this, "ncnt"] > 0) and __x_eq(__cpm[this, "ncnt"], __cpm[this, "count"])):
                return False
            # end if (line 112)
            if __x_cb(__x_cb(__x_ne(e, None)) and __x_iof(e, __cpm[this, "type"])):
                __r0 = this
                __r1 = __cpm[__r0, "ncnt"]
                __cpm[__r0, "ncnt"] = __x_inc(__r1)
                return True
            # end if (line 115)
            if __x_cb(__x_cb(__x_eq(__cpm[this, "count"], 0)) and (__x_cb(__cpm[this, "optional"]) or __cpm[this, "ncnt"]
 > 0)):
                return False
            # end if (line 121)
            if __x_cb(__x_cb(__x_eq(__cpm[this, "ncnt"], 0)) and __cpm[this, "optional"]):
                return False
            # end if (line 125)
            raise InternalError((u"malformed structure in ") + s + (u", expected ") + StrTool.str(__cpm[this, "type"]) + (u" but ") + StrTool\
.typeName(e) + (u" is met"))
        # end function __m_meet (line 111)

        def __m_meetEOF(this, s):
            if __x_cb(__x_cb(__cpm[this, "ncnt"] > 0) and __x_eq(__cpm[this, "ncnt"], __cpm[this, "count"])):
                return
            # end if (line 133)
            if __x_cb(__x_cb(__x_eq(__cpm[this, "count"], 0)) and (__x_cb(__cpm[this, "optional"]) or __cpm[this, "ncnt"]
 > 0)):
                return
            # end if (line 136)
            if __x_cb(__x_cb(__x_eq(__cpm[this, "ncnt"], 0)) and __cpm[this, "optional"]):
                return
            # end if (line 140)
            raise InternalError((u"malformed structure in ") + s + (u", expected ") + StrTool.str(__cpm[this, "type"]) + (u" but the end of the current element is met"))
        # end function __m_meetEOF (line 132)

        def __m_ElementPattern(this, type, count, optional):
            __csu(this)
            __cpm[this, "type"] = type
            __cpm[this, "count"] = count
            __cpm[this, "optional"] = optional
        # end function __m_ElementPattern (line 146)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 153)

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            __cpm[this, "ncnt"] = 0
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 159)

        __cpiT = __x_dpif("ElementPattern", {"__slots__": ("count", "ncnt", "optional", "type")})
        __clsT = __x_dcls("ElementPattern", __x_objT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), 
"meet": __m_meet, "meetEOF": __m_meetEOF, "reset": __m_reset, "__init__": __m_ElementPattern})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory ElementPattern, __c_ElementPattern (line 106)

    def __c_Range():
        def __m_Range(this, start, end, startLine, startColumn, endLine, endColumn):
            __csu(this)
            this.start = start
            this.end = end
            this.startLine = startLine
            this.startColumn = startColumn
            this.endLine = endLine
            this.endColumn = endColumn
        # end function __m_Range (line 176)

        def __n_fromAST(this, o):
            locs = o.loc
            rg = o.range
            return Range(rg[0], rg[1], locs.start.line, locs.start.column, locs.end.line, locs.end.column)
        # end function __n_fromAST (line 186)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 192)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 198)

        __clsT = __x_dcls("Range", __x_objT, {"__slots__": (), "fromAST": __n_fromAST, "__init__": __csi}, {"__slots__": (
"end", "endColumn", "endLine", "start", "startColumn", "startLine"), "__init__": __m_Range})
        return __clsT
    # end class factory Range, __c_Range (line 175)

    def __c_XMLDumper():
        def __m_init(this):
            __cpm[this, "attrs"] = StringMap()
            __cpm[this, "tagName"] = None
            __cpm[this, "crange"] = None
        # end function __m_init (line 210)

        def __m_tag(this, name):
            if __x_cb(__x_ne(__cpm[this, "tagName"], None)):
                raise InternalError((u"set the tagname again"))
            # end if (line 217)
            __cpm[this, "tagName"] = name
        # end function __m_tag (line 216)

        def __m_range(this, r):
            if __x_cb(__x_ne(__cpm[this, "crange"], None)):
                raise InternalError((u"set the range again"))
            # end if (line 224)
            __cpm[this, "crange"] = r
        # end function __m_range (line 223)

        def __m_attr(this, key, value):
            __cpm[this, "attrs"].set(key, StrTool.str(value))
        # end function __m_attr (line 230)

        def __m_finalize(this, e):
            def __f12_(v, n, o):
                def __f13_(c, k, z):
                    if __x_cb(__x_eq(c, (u"<"))):
                        c = (u"&lt;")
                    # end if (line 237)
                    if __x_cb(__x_eq(c, (u">"))):
                        c = (u"&gt;")
                    # end if (line 240)
                    if __x_cb(__x_eq(c, (u"&"))):
                        c = (u"&amp;")
                    # end if (line 243)
                    if __x_cb(__x_eq(c, (u"'"))):
                        c = (u"&apos;")
                    # end if (line 246)
                    if __x_cb(__x_eq(c, (u"\""))):
                        c = (u"&quot;")
                    # end if (line 249)
                    a.push(c)
                # end function <anonymous> (__f13_) (line 236)

                a.push((u" "))
                a.push(n)
                a.push((u"=\""))
                ArrayList(v).forEach(__f13_)
                a.push((u"\""))
            # end function <anonymous> (__f12_) (line 235)

            def __f14_(e, k, s):
                __u_has.val = True
                init()
                e.dump(self)
            # end function <anonymous> (__f14_) (line 262)

            __u_has = __x_var()
            ttag = __cpm[this, "tagName"]
            if __x_cb(__x_eq(ttag, None)):
                raise InternalError((u"tag name is required"))
            # end if (line 270)
            a = __cpm[this, "all"]
            a.push(__cpm[this, "makeTabs"](__cpm[this, "tabCnt"]) + (u"<") + ttag)
            __cpm[this, "attrs"].forEach(__f12_)
            if __x_cb(__x_ne(__cpm[this, "crange"], None)):
                a.push((u" start-line=\""))
                a.push(StrTool.str(__cpm[this, "crange"].startLine))
                a.push((u"\" start-column=\""))
                a.push(StrTool.str(__cpm[this, "crange"].startColumn))
                a.push((u"\" end-line=\""))
                a.push(StrTool.str(__cpm[this, "crange"].endLine))
                a.push((u"\" end-column=\""))
                a.push(StrTool.str(__cpm[this, "crange"].endColumn))
                a.push((u"\""))
            # end if (line 276)
            __cpm[this, "all"] = ArrayList()
            tc = __cpm[this, "tabCnt"]
            __cpm[this, "tabCnt"] = tc + 1
            __u_has.val = False
            init = __cpm[this, "init"]
            self = this
            e.forEachChild(__f14_)
            __cpm[this, "tabCnt"] = tc
            if __x_cb(__u_has.val):
                a.push((u">\n"))
                a.push(__cpm[this, "all"].join((u"")))
                a.push(__cpm[this, "makeTabs"](tc) + (u"</") + ttag + (u">"))
            else:
                a.push((u"/>"))
            # end if (line 295)
            a.push((u"\n"))
            __cpm[this, "all"] = a
        # end function __m_finalize (line 234)

        def __m_toString(this):
            return __cpm[this, "all"].join((u""))
        # end function __m_toString (line 306)

        def __m_XMLDumper(this):
            __csu(this)
            __cpm[this, "init"]()
        # end function __m_XMLDumper (line 310)

        def __m_makeTabs(this, n):
            ts = (u"  ")
            s = (u"")
            while True:
                __r0 = __x_cb
                __r1 = n
                n = __x_dec(__r1)
                if not __r0(__r1 > 0):
                    break
                # end if (line 322)
                s = s + ts
            # end while (line 318)
            return s
        # end function __m_makeTabs (line 315)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 330)

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            __cpm[this, "all"] = ArrayList()
            __cpm[this, "tabCnt"] = 0
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 336)

        __cpiT = __x_dpif("XMLDumper", {"__slots__": ("all", "attrs", "crange", "tabCnt", "tagName"), "init": __x_smet(__m_init), 
"makeTabs": __x_smet(__m_makeTabs)})
        __clsT = __x_dcls("XMLDumper", __x_objT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "attr": __m_attr, 
"finalize": __m_finalize, "range": __m_range, "tag": __m_tag, "toString": __m_toString, "__init__": __m_XMLDumper})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory XMLDumper, __c_XMLDumper (line 209)

    __r0 = __x_imp((u".compat"))
    ArrayList = __r0.ArrayList
    StrTool = __r0.StrTool
    printf = __r0.printf
    __r1 = __x_imp((u".StringMap"))
    StringMap = __r1.StringMap
    InternalError = __c_InternalError(Exception)
    CompileError = __c_CompileError(Exception)
    ConflictError = __c_ConflictError(CompileError)
    ElementPattern = __c_ElementPattern()
    Range = __c_Range()
    XMLDumper = __c_XMLDumper()
# program end


__()
