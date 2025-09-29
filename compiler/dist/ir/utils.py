# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, division, generators

__all__ = ("ElementPattern", "InternalError", "XMLDumper")


def __():
    from libyags0 import __x_tup, __x_tupof, __x_lst, __x_errT, __x_eq, __x_ne, __x_typ, __x_cb, __x_not, __x_iof, __x_inc, __x_dec, __x_var, __x_imf, __x_at_take, __x_at_drop, __x_at_forEach, __x_at_map, __x_at_filter, __x_at_flatMap, __x_at_some, __x_at_every, __x_at_find, __x_at_findIndex, __x_at_reduce, __x_at_join, __x_at_bind, __x_at_apply, __x_at_length, __x_at_isEmpty, __x_at_push, __x_at_pop, __x_at_shift, __x_at_unshift, __x_at_slice, __x_at_splice, __x_at_has, __x_dcls, __x_dpif, __x_dpsf, __x_prmT, __x_csgT, __x_cpgT, __x_objT, __x_smet, __x_prop, __x_tob, __x_tnb, Infinity, NaN
    __x_imp = __x_imf(__name__)
    global ElementPattern, InternalError, XMLDumper

    # function definitions:

    # class definitions:

    def __c_InternalError(__cexT):
        def __m_InternalError(this, message, *extras):
            __csu(this, message)
            this.extraInfo = extras
        # end function __m_InternalError

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __clsT = __x_dcls("InternalError", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": ("extraInfo",), 
"__init__": __m_InternalError})
        return __clsT
    # end class factory InternalError, __c_InternalError

    def __c_ElementPattern():
        def __m_reset(this):
            __cpm[this, "ncnt"] = 0
        # end function __m_reset

        def __m_meet(this, e, s):
            if __x_cb(__x_cb(__cpm[this, "ncnt"] > 0) and __x_eq(__cpm[this, "ncnt"], __cpm[this, "count"])):
                return False
            # end if
            if __x_cb(__x_cb(__x_ne(e, None)) and __x_iof(e, __cpm[this, "type"])):
                __r0 = this
                __r1 = __cpm[__r0, "ncnt"]
                __cpm[__r0, "ncnt"] = __x_inc(__r1)
                return True
            # end if
            if __x_cb(__x_cb(__x_eq(__cpm[this, "count"], 0)) and (__x_cb(__cpm[this, "optional"]) or __cpm[this, "ncnt"]
 > 0)):
                return False
            # end if
            if __x_cb(__x_cb(__x_eq(__cpm[this, "ncnt"], 0)) and __cpm[this, "optional"]):
                return False
            # end if
            raise InternalError((u"malformed structure in ") + s + (u", expected ") + StrTool.str(__cpm[this, "type"]) + (u" but ") + StrTool\
.typeName(e) + (u" is met"))
        # end function __m_meet

        def __m_meetEOF(this, s):
            if __x_cb(__x_cb(__cpm[this, "ncnt"] > 0) and __x_eq(__cpm[this, "ncnt"], __cpm[this, "count"])):
                return
            # end if
            if __x_cb(__x_cb(__x_eq(__cpm[this, "count"], 0)) and (__x_cb(__cpm[this, "optional"]) or __cpm[this, "ncnt"]
 > 0)):
                return
            # end if
            if __x_cb(__x_cb(__x_eq(__cpm[this, "ncnt"], 0)) and __cpm[this, "optional"]):
                return
            # end if
            raise InternalError((u"malformed structure in ") + s + (u", expected ") + StrTool.str(__cpm[this, "type"]) + (u" but the end of the current element is met"))
        # end function __m_meetEOF

        def __m_ElementPattern(this, type, count, optional):
            __csu(this)
            __cpm[this, "type"] = type
            __cpm[this, "count"] = count
            __cpm[this, "optional"] = optional
        # end function __m_ElementPattern

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            __cpm[this, "ncnt"] = 0
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __cpiT = __x_dpif("ElementPattern", {"__slots__": ("count", "ncnt", "optional", "type")})
        __clsT = __x_dcls("ElementPattern", __x_objT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), 
"meet": __m_meet, "meetEOF": __m_meetEOF, "reset": __m_reset, "__init__": __m_ElementPattern})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory ElementPattern, __c_ElementPattern

    def __c_XMLDumper():
        def __m_init(this):
            __cpm[this, "attrs"] = StringMap()
            __cpm[this, "tagName"] = None
            __cpm[this, "crange"] = None
        # end function __m_init

        def __m_tag(this, name):
            if __x_cb(__x_ne(__cpm[this, "tagName"], None)):
                raise InternalError((u"set the tagname again"))
            # end if
            __cpm[this, "tagName"] = name
        # end function __m_tag

        def __m_range(this, r):
            if __x_cb(__x_ne(__cpm[this, "crange"], None)):
                raise InternalError((u"set the range again"))
            # end if
            __cpm[this, "crange"] = r
        # end function __m_range

        def __m_attr(this, key, value):
            __cpm[this, "attrs"].set(key, StrTool.str(value))
        # end function __m_attr

        def __m_finalize(this, e):
            def __fI_(v, n, o):
                def __fJ_(c, k, z):
                    if __x_cb(__x_eq(c, (u"<"))):
                        c = (u"&lt;")
                    # end if
                    if __x_cb(__x_eq(c, (u">"))):
                        c = (u"&gt;")
                    # end if
                    if __x_cb(__x_eq(c, (u"&"))):
                        c = (u"&amp;")
                    # end if
                    if __x_cb(__x_eq(c, (u"'"))):
                        c = (u"&apos;")
                    # end if
                    if __x_cb(__x_eq(c, (u"\""))):
                        c = (u"&quot;")
                    # end if
                    a.push(c)
                # end function <anonymous> (__fJ_)

                a.push((u" "))
                a.push(n)
                a.push((u"=\""))
                ArrayList(v).forEach(__fJ_)
                a.push((u"\""))
            # end function <anonymous> (__fI_)

            def __fK_(e, k, s):
                __u_has.val = True
                init()
                e.dump(self)
            # end function <anonymous> (__fK_)

            __u_has = __x_var()
            ttag = __cpm[this, "tagName"]
            if __x_cb(__x_eq(ttag, None)):
                raise InternalError((u"tag name is required"))
            # end if
            a = __cpm[this, "all"]
            a.push(__cpm[this, "makeTabs"](__cpm[this, "tabCnt"]) + (u"<") + ttag)
            __cpm[this, "attrs"].forEach(__fI_)
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
            # end if
            __cpm[this, "all"] = ArrayList()
            tc = __cpm[this, "tabCnt"]
            __cpm[this, "tabCnt"] = tc + 1
            __u_has.val = False
            init = __cpm[this, "init"]
            self = this
            e.forEachChild(__fK_)
            __cpm[this, "tabCnt"] = tc
            if __x_cb(__u_has.val):
                a.push((u">\n"))
                a.push(__cpm[this, "all"].join((u"")))
                a.push(__cpm[this, "makeTabs"](tc) + (u"</") + ttag + (u">"))
            else:
                a.push((u"/>"))
            # end if
            a.push((u"\n"))
            __cpm[this, "all"] = a
        # end function __m_finalize

        def __m_toString(this):
            return __cpm[this, "all"].join((u""))
        # end function __m_toString

        def __m_XMLDumper(this):
            __csu(this)
            __cpm[this, "init"]()
        # end function __m_XMLDumper

        def __m_makeTabs(this, n):
            ts = (u"  ")
            s = (u"")
            while True:
                __r0 = __x_cb
                __r1 = n
                n = __x_dec(__r1)
                if not __r0(__r1 > 0):
                    break
                # end if
                s = s + ts
            # end while
            return s
        # end function __m_makeTabs

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            __cpm[this, "all"] = ArrayList()
            __cpm[this, "tabCnt"] = 0
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __cpiT = __x_dpif("XMLDumper", {"__slots__": ("all", "attrs", "crange", "tabCnt", "tagName"), "init": __x_smet(__m_init), 
"makeTabs": __x_smet(__m_makeTabs)})
        __clsT = __x_dcls("XMLDumper", __x_objT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "attr": __m_attr, 
"finalize": __m_finalize, "range": __m_range, "tag": __m_tag, "toString": __m_toString, "__init__": __m_XMLDumper})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory XMLDumper, __c_XMLDumper

    __r0 = __x_imp((u".compat"))
    ArrayList = __r0.ArrayList
    StrTool = __r0.StrTool
    printf = __r0.printf
    __r1 = __x_imp((u".StringMap"))
    StringMap = __r1.StringMap
    InternalError = __c_InternalError(Exception)
    ElementPattern = __c_ElementPattern()
    XMLDumper = __c_XMLDumper()
# program end


__()
