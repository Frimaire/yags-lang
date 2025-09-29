# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, division, generators

__all__ = ("BuiltinVar", "ClassTag", "FunctionExpTag", "FunctionTag", "GlobalVar", "LocalVar", "MethodTag", \
"TempVar", "VarReference", "Variable", "encodeRadix32")


def __():
    from libyags0 import __x_tup, __x_tupof, __x_lst, __x_errT, __x_eq, __x_ne, __x_typ, __x_cb, __x_not, __x_iof, __x_inc, __x_dec, __x_var, __x_imf, __x_at_take, __x_at_drop, __x_at_forEach, __x_at_map, __x_at_filter, __x_at_flatMap, __x_at_some, __x_at_every, __x_at_find, __x_at_findIndex, __x_at_reduce, __x_at_join, __x_at_bind, __x_at_apply, __x_at_length, __x_at_isEmpty, __x_at_push, __x_at_pop, __x_at_shift, __x_at_unshift, __x_at_slice, __x_at_splice, __x_at_has, __x_dcls, __x_dpif, __x_dpsf, __x_prmT, __x_csgT, __x_cpgT, __x_objT, __x_smet, __x_prop, __x_tob, __x_tnb, Infinity, NaN
    __x_imp = __x_imf(__name__)
    global BuiltinVar, ClassTag, FunctionExpTag, FunctionTag, GlobalVar, LocalVar, MethodTag, TempVar, VarReference, \
Variable, encodeRadix32

    # function definitions:

    def encodeRadix32(n):
        if __x_cb(__x_cb(__x_ne(int(n), n)) or n < 0):
            raise InternalError((u"illegal n in encodeRadix32"))
        # end if
        if __x_cb(n >= 1 << 30):
            raise InternalError((u"n too large in encodeRadix32"))
        # end if
        if __x_cb(__x_eq(n, 0)):
            return (u"0")
        # end if
        k = 6
        s = (u"")
        while __x_cb(__x_cb(k > 0) and n > 0):
            __r0 = k
            k = __x_dec(__r0)
            cn = radix36.get(n & 31)
            s = cn + s
            n = n >> 5
        # end while
        return s
    # end function encodeRadix32

    # class definitions:

    def __c_Variable():
        def __g_isSpecial(this):
            return __x_cb(__v___isKeyword(this.name)) or __v___isSpecial(this.name)
        # end function __g_isSpecial

        def __m_encode(this):
            def __f5_(c, k, a):
                ch = StrTool.codePointAt(c)
                if __x_cb(__x_eq(ch, 36)):
                    __u_se.val = __u_se.val + (u"_d")
                    return
                # end if
                if __x_cb(__x_eq(ch, 95)):
                    __u_se.val = __u_se.val + (u"__")
                    return
                # end if
                if __x_cb(ch < 128):
                    __u_se.val = __u_se.val + c
                    return
                # end if
                pn = ch >> 15
                cn = ch
                ss = (u"")
                ss = radix36.get(cn & 31) + ss
                cn = cn >> 5
                ss = radix36.get(cn & 31) + ss
                cn = cn >> 5
                ss = radix36.get(cn & 31) + ss
                ss = radix36.get(pn) + ss
                __u_se.val = __u_se.val + ((u"_") + ss)
            # end function <anonymous> (__f5_)

            __u_se = __x_var()
            __u_se.val = (u"")
            ArrayList(this.name).forEach(__f5_)
            return __u_se.val
        # end function __m_encode

        def __m_redeclare(this, __v_from, range = (None)):
            if __x_cb(__x_ne(__v_from, this.at)):
                raise InternalError((u"redeclare in defferent function scope"))
            # end if
        # end function __m_redeclare

        def __m_read(this, __v_from, range = (None)):
            raise InternalError((u"read check is abstract"))
        # end function __m_read

        def __m_write(this, __v_from, range = (None)):
            raise InternalError((u"write check is abstract"))
        # end function __m_write

        def __m_toPython(this):
            return this.toRawPython()
        # end function __m_toPython

        def __m_toRawPython(this):
            raise InternalError((u"toRawPython is abstract"))
        # end function __m_toRawPython

        def __m_toComment(this):
            n = this.name
            s = this.toRawPython()
            if __x_cb(this.isSpecial):
                return n + (u"(") + s + (u")")
            # end if
            return s
        # end function __m_toComment

        def __m_____str____(this):
            return this.toString()
        # end function __str__(__m_____str____)

        def __m_toString(this):
            return this.name
        # end function __m_toString

        def __m_Variable(this, name, at, range):
            __csu(this)
            this.name = name
            this.range = range
            this.at = at
        # end function __m_Variable

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # initialize properties
            this.assigned = False
            this.closure = False
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __clsT = __x_dcls("Variable", __x_objT, {"__slots__": (), "__init__": __csi}, {"__slots__": ("assigned", 
"at", "closure", "name", "range"), "__str__": __m_____str____, "encode": __m_encode, "isSpecial": __x_prop(__g_isSpecial, None), 
"read": __m_read, "redeclare": __m_redeclare, "toComment": __m_toComment, "toPython": __m_toPython, "toRawPython": __m_toRawPython, 
"toString": __m_toString, "write": __m_write, "__init__": __m_Variable})
        return __clsT
    # end class factory Variable, __c_Variable

    def __c_BuiltinVar(__cexT):
        def __m_redeclare(this, __v_from, range = (None)):
            raise InternalError((u"redeclare BuiltinVar"))
        # end function __m_redeclare

        def __m_read(this, __v_from, range = (None)):
            pass
        # end function __m_read

        def __m_write(this, __v_from, range = (None)):
            CAS.error(range, (u"Illegal assignment to bulit-in variables"))
        # end function __m_write

        def __m_toRawPython(this):
            return this.name
        # end function __m_toRawPython

        def __m_toString(this):
            return (u"builtin_var.") + this.name
        # end function __m_toString

        def __m_BuiltinVar(this, name, at):
            __csu(this, name, at, None)
        # end function __m_BuiltinVar

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

        __clsT = __x_dcls("BuiltinVar", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "read": __m_read, 
"redeclare": __m_redeclare, "toRawPython": __m_toRawPython, "toString": __m_toString, "write": __m_write, 
"__init__": __m_BuiltinVar})
        return __clsT
    # end class factory BuiltinVar, __c_BuiltinVar

    def __c_LocalVar(__cexT):
        def __g_isSpecial(this):
            if __x_cb(__x_cb(__x_cb(StrTool.strlen(this.name) > 2) and __x_eq(StrTool.codePointAt(this.name, 0), 
95)) and __x_eq(StrTool.codePointAt(this.name, 0), 95)):
                return True
            # end if
            return (super(__clsT, this)).isSpecial
        # end function __g_isSpecial

        def __m_redeclare(this, __v_from, range = (None)):
            (super(__clsT, this)).redeclare(__v_from, range)
        # end function __m_redeclare

        def __m_read(this, __v_from, range = (None)):
            pass
        # end function __m_read

        def __m_write(this, __v_from, range = (None)):
            this.assigned = True
            if __x_cb(__x_ne(__v_from, this.at)):
                this.closure = True
            # end if
        # end function __m_write

        def __m_toRawPython(this):
            if __x_cb(this.closure):
                return (u"__u_") + this.encode()
            # end if
            return this.toOriginPython()
        # end function __m_toRawPython

        def __m_toPython(this):
            clsuf = (u".val") if __x_cb(this.closure) else (u"")
            return this.toRawPython() + clsuf
        # end function __m_toPython

        def __m_toOriginPython(this):
            if __x_cb(__x_not(this.isSpecial)):
                return this.name
            # end if
            return (u"__v_") + this.encode()
        # end function __m_toOriginPython

        def __m_toString(this):
            n = this.name
            return (u"local_var[") + hex(id(this)) + (u"].") + ((u"?") if __x_cb(__x_eq(n, None)) else n) + ((u".closure")
 if __x_cb(this.closure) else (u""))
        # end function __m_toString

        def __m_LocalVar(this, name, range):
            __csu(this, name, None, range)
        # end function __m_LocalVar

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

        __clsT = __x_dcls("LocalVar", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "isSpecial": __x_prop(__g_isSpecial, None), 
"read": __m_read, "redeclare": __m_redeclare, "toOriginPython": __m_toOriginPython, "toPython": __m_toPython, 
"toRawPython": __m_toRawPython, "toString": __m_toString, "write": __m_write, "__init__": __m_LocalVar})
        return __clsT
    # end class factory LocalVar, __c_LocalVar

    def __c_VarReference(__cexT):
        def __m_redeclare(this, __v_from, range = (None)):
            CAS.note(this.range, (u"An internal error occurs here"))
            raise InternalError((u"declare VarReference"))
        # end function __m_redeclare

        def __g_tempVarOnly(this):
            return __x_cb(__x_ne(__cpm[this, "target"], None)) and __x_iof(__cpm[this, "target"], FunctionTag)
        # end function __g_tempVarOnly

        def __m_read(this, __v_from, range = (None)):
            if __x_cb(__x_eq(this.at, None)):
                CAS.note(this.range, (u"An internal error occurs here"))
                raise InternalError((u"at is null"))
            # end if
            if __x_cb(__x_eq(__cpm[this, "target"], None)):
                __cpm[this, "target"] = this.at.referVar(this.name, this.range)
            # end if
            __cpm[this, "target"].read(__v_from, range)
        # end function __m_read

        def __m_write(this, __v_from, range = (None)):
            if __x_cb(__x_eq(this.at, None)):
                CAS.note(this.range, (u"An internal error occurs here"))
                raise InternalError((u"at is null"))
            # end if
            if __x_cb(__x_eq(__cpm[this, "target"], None)):
                __cpm[this, "target"] = this.at.referVar(this.name, this.range)
            # end if
            __cpm[this, "target"].write(__v_from, range)
        # end function __m_write

        def __m_toPython(this):
            if __x_cb(__x_eq(this.at, None)):
                CAS.note(this.range, (u"An internal error occurs here"))
                raise InternalError((u"at is null"))
            # end if
            if __x_cb(__x_eq(__cpm[this, "target"], None)):
                CAS.note(this.range, (u"An internal error occurs here"))
                raise InternalError((u"unreferenced variable ") + str(this.name))
            # end if
            return __cpm[this, "target"].toPython()
        # end function __m_toPython

        def __m_toRawPython(this):
            if __x_cb(__x_eq(__cpm[this, "target"], None)):
                CAS.note(this.range, (u"An internal error occurs here"))
                raise InternalError((u"unreferenced variable ") + str(this.name))
            # end if
            return __cpm[this, "target"].toRawPython()
        # end function __m_toRawPython

        def __m_toComment(this):
            if __x_cb(__x_eq(__cpm[this, "target"], None)):
                CAS.note(this.range, (u"An internal error occurs here"))
                return (u"<unreferenced variable>")
            # end if
            return __cpm[this, "target"].toComment()
        # end function __m_toComment

        def __m_toString(this):
            n = this.name
            return (u"ref[") + hex(id(this)) + (u"].") + ((u"?") if __x_cb(__x_eq(n, None)) else n) + (u"[") + ((u"null")
 if __x_cb(__x_eq(__cpm[this, "target"], None)) else hex(id(__cpm[this, "target"]))) + (u"]")
        # end function __m_toString

        def __m_VarReference(this, name, range):
            __csu(this, name, None, range)
            __cpm[this, "target"] = None
        # end function __m_VarReference

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __cpiT = __x_dpif("VarReference", {"__slots__": ("target",)})
        __clsT = __x_dcls("VarReference", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "read": __m_read, 
"redeclare": __m_redeclare, "tempVarOnly": __x_prop(__g_tempVarOnly, None), "toComment": __m_toComment, 
"toPython": __m_toPython, "toRawPython": __m_toRawPython, "toString": __m_toString, "write": __m_write, 
"__init__": __m_VarReference})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory VarReference, __c_VarReference

    def __c_ClassTag(__cexT):
        def __m_redeclare(this, __v_from, range = (None)):
            CAS.conflict(this.name, this.range, range)
        # end function __m_redeclare

        def __m_write(this, __v_from, range = (None)):
            CAS.delayedError(range, (u"Illegal assignment to class definition %s."), this.name)
            CAS.note(this.range, (u"'%s' has previously declared here."), this.name)
        # end function __m_write

        def __m_toPython(this):
            return this.toRawPython()
        # end function __m_toPython

        def __m_toString(this):
            n = this.name
            f = this.at
            return (u"class.") + ((u"?") if __x_cb(__x_eq(n, None)) else n) + ((u"") if __x_cb(__x_eq(f, None)) else 
(u"[") + this.at.functionToken + (u"]"))
        # end function __m_toString

        def __m_toFactoryName(this):
            return (u"__c_") + this.encode()
        # end function __m_toFactoryName

        def __m_ClassTag(this, name, range):
            __csu(this, name, range)
            this.assigned = True
        # end function __m_ClassTag

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

        __clsT = __x_dcls("ClassTag", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "redeclare": __m_redeclare, 
"toFactoryName": __m_toFactoryName, "toPython": __m_toPython, "toString": __m_toString, "write": __m_write, 
"__init__": __m_ClassTag})
        return __clsT
    # end class factory ClassTag, __c_ClassTag

    def __c_FunctionTag(__cexT):
        def __m_read(this, __v_from, range = (None)):
            pass
        # end function __m_read

        def __m_redeclare(this, __v_from, range = (None)):
            CAS.conflict(this.name, this.range, range)
        # end function __m_redeclare

        def __m_write(this, __v_from, range = (None)):
            CAS.delayedError(range, (u"Illegal assignment to function definition %s."), this.name)
            CAS.note(this.range, (u"'%s' has previously declared here."), this.name)
        # end function __m_write

        def __m_toPython(this):
            return this.toRawPython()
        # end function __m_toPython

        def __m_toString(this):
            n = this.name
            f = this.at
            return (u"func[") + hex(id(this)) + (u"].") + ((u"?") if __x_cb(__x_eq(n, None)) else n)
        # end function __m_toString

        def __m_FunctionTag(this, name, range):
            __csu(this, name, range)
            this.assigned = True
        # end function __m_FunctionTag

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

        __clsT = __x_dcls("FunctionTag", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "read": __m_read, 
"redeclare": __m_redeclare, "toPython": __m_toPython, "toString": __m_toString, "write": __m_write, "__init__": __m_FunctionTag})
        return __clsT
    # end class factory FunctionTag, __c_FunctionTag

    def __c_FunctionExpTag(__cexT):
        def __m_write(this, __v_from, range = (None)):
            CAS.delayedError(range, (u"Illegal assignment to function expression name %s"), this.name)
            CAS.note(this.range, (u"'%s' has previously defined here."), this.name)
        # end function __m_write

        def __m_toRawPython(this):
            n = this.name
            s = (u"__f") + this.at.functionToken + (u"_")
            return s if __x_cb(__x_eq(n, None)) else s + this.encode()
        # end function __m_toRawPython

        def __m_toComment(this):
            n = this.name
            s = this.toRawPython()
            if __x_cb(__x_eq(n, None)):
                n = (u"<anonymous>")
            # end if
            return n + (u" (") + s + (u")")
        # end function __m_toComment

        def __m_toString(this):
            n = this.name
            f = this.at
            return (u"func_exp[") + hex(id(this)) + (u"].") + ((u"anonymous") if __x_cb(__x_eq(n, None)) else n)
        # end function __m_toString

        def __m_FunctionExpTag(this, name = (None), range = (None)):
            __csu(this, name, range)
        # end function __m_FunctionExpTag

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

        __clsT = __x_dcls("FunctionExpTag", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "toComment": __m_toComment, 
"toRawPython": __m_toRawPython, "toString": __m_toString, "write": __m_write, "__init__": __m_FunctionExpTag})
        return __clsT
    # end class factory FunctionExpTag, __c_FunctionExpTag

    def __c_GlobalVar(__cexT):
        def __m_redeclare(this, __v_from, range = (None)):
            raise InternalError((u"redeclare GlobalVar"))
        # end function __m_redeclare

        def __m_read(this, __v_from, range = (None)):
            pass
        # end function __m_read

        def __m_write(this, __v_from, range = (None)):
            raise InternalError((u"Illegal assignment to superglobal variables"))
        # end function __m_write

        def __m_toRawPython(this):
            return this.name
        # end function __m_toRawPython

        def __m_toString(this):
            n = this.name
            return (u"global.") + ((u"?") if __x_cb(__x_eq(n, None)) else n)
        # end function __m_toString

        def __m_GlobalVar(this, name):
            __csu(this, name, None, None)
            this.assigned = True
        # end function __m_GlobalVar

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

        __clsT = __x_dcls("GlobalVar", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "read": __m_read, 
"redeclare": __m_redeclare, "toRawPython": __m_toRawPython, "toString": __m_toString, "write": __m_write, 
"__init__": __m_GlobalVar})
        return __clsT
    # end class factory GlobalVar, __c_GlobalVar

    def __c_MethodTag(__cexT):
        def __m_read(this, __v_from, range = (None)):
            pass
        # end function __m_read

        def __m_redeclare(this, __v_from, range = (None)):
            raise InternalError((u"declaration of method tag"))
        # end function __m_redeclare

        def __m_toRawPython(this):
            pf = (((u"t") if __x_cb(this.isSetter) else (u"h")) if __x_cb(this.isAccessor) else (u"n")) if __x_cb\
(this.isStatic) else (((u"s") if __x_cb(this.isSetter) else (u"g")) if __x_cb(this.isAccessor) else (u"m")
)
            return (u"__") + pf + (u"_") + this.encode()
        # end function __m_toRawPython

        def __m_toString(this):
            n = this.name
            return (u"method.") + ((u"public.") if __x_cb(this.isPublic) else (u"private.")) + ((u"static.") if __x_cb
(this.isStatic) else (u"")) + (((u"setter") if __x_cb(this.isSetter) else (u"getter")) if __x_cb(this\
.isAccessor) else (u"method")) + (u".") + ((u"?") if __x_cb(__x_eq(n, None)) else n)
        # end function __m_toString

        def __m_MethodTag(this, name, range, methodType, isStatic, isPublic):
            __csu(this, name, range)
            am = StringMap([[(u"method"), False], [(u"get"), True], [(u"set"), True]])
            this.isAccessor = am.get(methodType)
            this.isSetter = __x_eq(methodType, (u"set"))
            this.isStatic = isStatic
            this.isPublic = isPublic
        # end function __m_MethodTag

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

        __clsT = __x_dcls("MethodTag", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": ("isAccessor", 
"isPublic", "isSetter", "isStatic"), "read": __m_read, "redeclare": __m_redeclare, "toRawPython": __m_toRawPython, 
"toString": __m_toString, "__init__": __m_MethodTag})
        return __clsT
    # end class factory MethodTag, __c_MethodTag

    def __c_TempVar(__cexT):
        def __m_toRawPython(this):
            return (u"__r") + encodeRadix32(this.index)
        # end function __m_toRawPython

        def __m_toString(this):
            return (u"temp[") + hex(id(this)) + (u"][") + StrTool.str(this.index) + (u"]")
        # end function __m_toString

        def __m_TempVar(this, index, at):
            __csu(this, None, at, None)
            this.assigned = True
            this.index = index
        # end function __m_TempVar

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

        __clsT = __x_dcls("TempVar", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": ("index",), 
"toRawPython": __m_toRawPython, "toString": __m_toString, "__init__": __m_TempVar})
        return __clsT
    # end class factory TempVar, __c_TempVar

    __r0 = __x_imp((u".compat"))
    ArrayList = __r0.ArrayList
    StrTool = __r0.StrTool
    printf = __r0.printf
    __r1 = __x_imp((u".StringMap"))
    StringMap = __r1.StringMap
    __r2 = __x_imp((u".utils"))
    ElementPattern = __r2.ElementPattern
    InternalError = __r2.InternalError
    XMLDumper = __r2.XMLDumper
    CAS = __x_imp((u"tools.cas"))
    __r3 = __x_imp((u".attribute"))
    __v___isKeyword = __r3.isKeyword
    __v___isSpecial = __r3.isSpecial
    radix36 = ArrayList((u"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    Variable = __c_Variable()
    BuiltinVar = __c_BuiltinVar(Variable)
    LocalVar = __c_LocalVar(Variable)
    VarReference = __c_VarReference(Variable)
    ClassTag = __c_ClassTag(LocalVar)
    FunctionTag = __c_FunctionTag(LocalVar)
    FunctionExpTag = __c_FunctionExpTag(FunctionTag)
    GlobalVar = __c_GlobalVar(Variable)
    MethodTag = __c_MethodTag(FunctionTag)
    TempVar = __c_TempVar(Variable)
# program end


__()
