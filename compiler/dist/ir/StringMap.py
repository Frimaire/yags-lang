# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, division, generators

__all__ = ("StringMap",)


def __():
    from libyags0 import __x_tup, __x_tupof, __x_lst, __x_errT, __x_eq, __x_ne, __x_typ, __x_cb, __x_not, __x_iof, __x_inc, __x_dec, __x_var, __x_imf, __x_at_take, __x_at_drop, __x_at_forEach, __x_at_map, __x_at_filter, __x_at_flatMap, __x_at_some, __x_at_every, __x_at_find, __x_at_findIndex, __x_at_reduce, __x_at_join, __x_at_bind, __x_at_apply, __x_at_length, __x_at_isEmpty, __x_at_push, __x_at_pop, __x_at_shift, __x_at_unshift, __x_at_slice, __x_at_splice, __x_dcls, __x_dpif, __x_dpsf, __x_prmT, __x_csgT, __x_cpgT, __x_objT, __x_smet, __x_prop, __x_tob, __x_tnb, Infinity, NaN
    __x_imp = __x_imf(__name__)
    global StringMap

    # function definitions:

    def chkKey(s):
        if __x_cb(__x_not(__x_iof(s, type((u""))))):
            raise TypeError((u"key is not a string"))
        # end if (line 15)
        return s
    # end function chkKey (line 14)

    # class definitions:

    def __c_StringMap():
        def __m_StringMap(this, source = (None)):
            def __f4_(g, i, a):
                k = chkKey(g[0])
                v = g[1]
                if __x_cb(this.has(k)):
                    raise AttributeError((u"key ") + k + (u" is existed"))
                # end if (line 28)
                this.set(k, v)
            # end function <anonymous> (__f4_) (line 25)

            __csu(this)
            __cpm[this, "o"] = ({})
            ArrayList(source).forEach(__f4_)
        # end function __m_StringMap (line 24)

        def __m_get(this, key, *defval):
            dfv = ArrayList(defval)
            if __x_cb(dfv.length >= 2):
                raise TypeError((u"Only one default value is allowed"))
            # end if (line 41)
            key = chkKey(key)
            if __x_cb(__x_eq(dfv.length, 0)):
                return __cpm[this, "o"][key]
            # end if (line 45)
            return __cpm[this, "o"].get(key, dfv.get(0))
        # end function __m_get (line 39)

        def __m_set(this, key, value):
            key = chkKey(key)
            __r0 = __cpm[this, "o"]
            __r1 = key
            __r0[__r1] = value
            return this
        # end function __m_set (line 51)

        def __m_sets(this, keys, value):
            def __f8_(k, n, a):
                this.set(k, value)
            # end function <anonymous> (__f8_) (line 60)

            ArrayList(keys).forEach(__f8_)
            return this
        # end function __m_sets (line 59)

        def __m_has(this, key):
            key = chkKey(key)
            return __cpm[this, "o"].__contains__(key)
        # end function __m_has (line 68)

        def __m_remove(this, key):
            key = chkKey(key)
            if __x_cb(__x_not(this.has(key))):
                raise AttributeError((u"key ") + key + (u" doesn't exist"))
            # end if (line 75)
            del __cpm[this, "o"][key]
            return this
        # end function __m_remove (line 73)

        def __m_forEach(this, callback):
            def __fC_(i, k, a):
                if __x_cb(__x_eq(callback(__cpm[this, "o"][i], i, this), False)):
                    return False
                # end if (line 84)
            # end function <anonymous> (__fC_) (line 83)

            __r0 = []
            __r0.extend(__cpm[this, "o"])
            a0 = __r0
            a0.sort()
            ArrayList(a0).forEach(__fC_)
        # end function __m_forEach (line 82)

        def __g_length(this):
            return len(__cpm[this, "o"])
        # end function __g_length (line 96)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 100)

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 106)

        __cpiT = __x_dpif("StringMap", {"__slots__": ("o",)})
        __clsT = __x_dcls("StringMap", __x_objT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "forEach": __m_forEach, 
"get": __m_get, "has": __m_has, "length": __x_prop(__g_length, None), "remove": __m_remove, "set": __m_set, 
"sets": __m_sets, "__init__": __m_StringMap})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory StringMap, __c_StringMap (line 23)

    __r0 = __x_imp((u".compat"))
    ArrayList = __r0.ArrayList
    StringMap = __c_StringMap()
# program end


__()
