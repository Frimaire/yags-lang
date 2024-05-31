# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, division, generators

__all__ = ("Attribute", "BuiltinVar", "ClassFieldDescriptor", "ClassTag", "FunctionExpTag", "FunctionTag", \
"GlobalVar", "Identifier", "LocalVar", "MethodTag", "TempVar", "Variable")


def __():
    from libyags0 import __x_tup, __x_tupof, __x_lst, __x_errT, __x_eq, __x_ne, __x_typ, __x_cb, __x_not, __x_iof, __x_inc, __x_dec, __x_var, __x_imf, __x_at_take, __x_at_drop, __x_at_forEach, __x_at_map, __x_at_filter, __x_at_flatMap, __x_at_some, __x_at_every, __x_at_find, __x_at_findIndex, __x_at_reduce, __x_at_join, __x_at_bind, __x_at_apply, __x_at_length, __x_at_isEmpty, __x_at_push, __x_at_pop, __x_at_shift, __x_at_unshift, __x_at_slice, __x_at_splice, __x_dcls, __x_dpif, __x_dpsf, __x_prmT, __x_csgT, __x_cpgT, __x_objT, __x_smet, __x_prop, __x_tob, __x_tnb, Infinity, NaN
    __x_imp = __x_imf(__name__)
    global Attribute, BuiltinVar, ClassFieldDescriptor, ClassTag, FunctionExpTag, FunctionTag, GlobalVar, \
Identifier, LocalVar, MethodTag, TempVar, Variable

    # function definitions:

    # class definitions:

    def __c_Identifier():
        def __n_encodeRadix32(this, n):
            if __x_cb(__x_cb(__x_ne(int(n), n)) or n < 0):
                raise InternalError((u"illegal n in encodeRadix32"))
            # end if (line 20)
            if __x_cb(n >= 1 << 30):
                raise InternalError((u"n too large in encodeRadix32"))
            # end if (line 23)
            if __x_cb(__x_eq(n, 0)):
                return (u"0")
            # end if (line 26)
            k = 6
            s = (u"")
            while __x_cb(__x_cb(k > 0) and n > 0):
                __r0 = k
                k = __x_dec(__r0)
                cn = Identifier.radix36.get(n & 31)
                s = cn + s
                n = n >> 5
            # end while (line 31)
            return s
        # end function __n_encodeRadix32 (line 19)

        def __g_isKeyword(this):
            return Identifier.pythonKeywords.has(this.name)
        # end function __g_isKeyword (line 41)

        def __g_isSpecial(this):
            def __f5_(c, k, a):
                ch = StrTool.codePointAt(c)
                if __x_cb(__x_eq(ch, 36)):
                    __u_enc.val = True
                    return False
                # end if (line 48)
                if __x_cb(ch >= 128):
                    __u_enc.val = True
                    return False
                # end if (line 52)
            # end function <anonymous> (__f5_) (line 46)

            __u_enc = __x_var()
            __u_enc.val = False
            ars = ArrayList(this.name)
            ars.forEach(__f5_)
            return __u_enc.val
        # end function __g_isSpecial (line 45)

        def __m_encode(this):
            def __f7_(c, k, a):
                ch = StrTool.codePointAt(c)
                if __x_cb(__x_eq(ch, 36)):
                    __u_se.val = __u_se.val + (u"_d")
                    return
                # end if (line 68)
                if __x_cb(__x_eq(ch, 95)):
                    __u_se.val = __u_se.val + (u"__")
                    return
                # end if (line 72)
                if __x_cb(ch < 128):
                    __u_se.val = __u_se.val + c
                    return
                # end if (line 76)
                pn = ch >> 15
                cn = ch
                ss = (u"")
                ss = Identifier.radix36.get(cn & 31) + ss
                cn = cn >> 5
                ss = Identifier.radix36.get(cn & 31) + ss
                cn = cn >> 5
                ss = Identifier.radix36.get(cn & 31) + ss
                ss = Identifier.radix36.get(pn) + ss
                __u_se.val = __u_se.val + ((u"_") + ss)
            # end function <anonymous> (__f7_) (line 66)

            __u_se = __x_var()
            __u_se.val = (u"")
            ArrayList(this.name).forEach(__f7_)
            return __u_se.val
        # end function __m_encode (line 65)

        def __m_toString(this):
            return this.name
        # end function __m_toString (line 98)

        def __m_Identifier(this, name, range):
            __csu(this)
            this.name = name
            this.range = range
        # end function __m_Identifier (line 102)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
            this.radix36 = ArrayList((u"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
            this.pythonKeywords = StringMap()
        # end static initializer __csi (line 108)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 116)

        __clsT = __x_dcls("Identifier", __x_objT, {"__slots__": ("pythonKeywords", "radix36"), "encodeRadix32": __n_encodeRadix32, 
"__init__": __csi}, {"__slots__": ("name", "range"), "encode": __m_encode, "isKeyword": __x_prop(__g_isKeyword, None), 
"isSpecial": __x_prop(__g_isSpecial, None), "toString": __m_toString, "__init__": __m_Identifier})
        return __clsT
    # end class factory Identifier, __c_Identifier (line 18)

    def __c_Attribute(__cexT):
        def __m_toPython(this):
            return this.name
        # end function __m_toPython (line 129)

        def __m_Attribute(this, name, range):
            __csu(this, name, range)
            if __x_cb(this.isSpecial):
                raise CompileError((u"Illegal attribute name ") + name, range)
            # end if (line 135)
            if __x_cb(this.isKeyword):
                raise CompileError((u"Python keyword cannot be used as attribute ") + name, range)
            # end if (line 138)
        # end function __m_Attribute (line 133)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 143)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 149)

        __clsT = __x_dcls("Attribute", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "toPython": __m_toPython, 
"__init__": __m_Attribute})
        return __clsT
    # end class factory Attribute, __c_Attribute (line 128)

    def __c_Variable(__cexT):
        def __g_isSpecial(this):
            return __x_cb((super(__clsT, this)).isSpecial) or (super(__clsT, this)).isKeyword
        # end function __g_isSpecial (line 161)

        def __m_redeclare(this, __v_from, range = (None)):
            if __x_cb(__x_ne(__v_from, this.at)):
                raise InternalError((u"redeclare in defferent function scope"))
            # end if (line 166)
        # end function __m_redeclare (line 165)

        def __m_read(this, __v_from, range = (None)):
            raise InternalError((u"read check is abstract"))
        # end function __m_read (line 171)

        def __m_write(this, __v_from, range = (None)):
            raise InternalError((u"write check is abstract"))
        # end function __m_write (line 175)

        def __m_toPython(this):
            return this.toRawPython()
        # end function __m_toPython (line 179)

        def __m_toRawPython(this):
            raise InternalError((u"toRawPython is abstract"))
        # end function __m_toRawPython (line 183)

        def __m_toComment(this):
            n = this.name
            s = this.toRawPython()
            if __x_cb(this.isSpecial):
                return n + (u"(") + s + (u")")
            # end if (line 190)
            return s
        # end function __m_toComment (line 187)

        def __m_Variable(this, name, at, range):
            __csu(this, name, range)
            this.at = at
        # end function __m_Variable (line 196)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 201)

        def __csu(this, *argv):
            # initialize properties
            this.assigned = False
            this.closure = False
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 207)

        __clsT = __x_dcls("Variable", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": ("assigned", 
"at", "closure"), "isSpecial": __x_prop(__g_isSpecial, None), "read": __m_read, "redeclare": __m_redeclare, 
"toComment": __m_toComment, "toPython": __m_toPython, "toRawPython": __m_toRawPython, "write": __m_write, 
"__init__": __m_Variable})
        return __clsT
    # end class factory Variable, __c_Variable (line 160)

    def __c_BuiltinVar(__cexT):
        def __m_redeclare(this, __v_from, range = (None)):
            raise InternalError((u"redeclare BuiltinVar"))
        # end function __m_redeclare (line 223)

        def __m_read(this, __v_from, range = (None)):
            pass
        # end function __m_read (line 227)

        def __m_write(this, __v_from, range = (None)):
            raise CompileError((u"Illegal assignment to bulit-in variables"), range)
        # end function __m_write (line 231)

        def __m_toRawPython(this):
            return this.name
        # end function __m_toRawPython (line 235)

        def __m_toString(this):
            return (u"builtin_var.") + this.name
        # end function __m_toString (line 239)

        def __m_BuiltinVar(this, name, at):
            __csu(this, name, at, None)
        # end function __m_BuiltinVar (line 243)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 247)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 253)

        __clsT = __x_dcls("BuiltinVar", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "read": __m_read, 
"redeclare": __m_redeclare, "toRawPython": __m_toRawPython, "toString": __m_toString, "write": __m_write, 
"__init__": __m_BuiltinVar})
        return __clsT
    # end class factory BuiltinVar, __c_BuiltinVar (line 222)

    def __c_ClassFieldDescriptor(__cexT):
        def __g_isProperty(this):
            __cpm[this, "verify"]()
            return __cpm[this, "property"]
        # end function __g_isProperty (line 266)

        def __g_isAccessor(this):
            __cpm[this, "verify"]()
            return __x_cb(__x_ne(__cpm[this, "getter"], None)) or __x_ne(__cpm[this, "setter"], None)
        # end function __g_isAccessor (line 271)

        def __g_isGetter(this):
            __cpm[this, "verify"]()
            return __x_ne(__cpm[this, "getter"], None)
        # end function __g_isGetter (line 276)

        def __g_isSetter(this):
            __cpm[this, "verify"]()
            return __x_ne(__cpm[this, "setter"], None)
        # end function __g_isSetter (line 281)

        def __g_isMethod(this):
            __cpm[this, "verify"]()
            return __x_ne(__cpm[this, "method"], None)
        # end function __g_isMethod (line 286)

        def __g_isPrivate(this):
            __cpm[this, "verify"]()
            return __cpm[this, "priv"]
        # end function __g_isPrivate (line 291)

        def __m_meetMethod(this, tag):
            if __x_cb(__x_ne(__cpm[tag, "isStatic"], __cpm[this, "isStatic"])):
                raise InternalError((u"mismatched static flag"))
            # end if (line 297)
            if __x_cb(__cpm[this, "property"]):
                raise ConflictError((u"Incompatible override to property %s"), tag.range, this.range, this.name)
            # end if (line 300)
            if __x_cb(__x_cb(__x_cb(__x_cb(__x_ne(__cpm[this, "method"], None)) or (__x_cb(__x_cb(__x_ne(__cpm[this
, "setter"], None)) or __x_ne(__cpm[this, "getter"], None)) and __x_not(tag.isAccessor))) or (__x_cb(__x_ne(__cpm[this
, "setter"], None)) and tag.isSetter)) or (__x_cb(__x_ne(__cpm[this, "getter"], None)) and __x_not(tag\
.isSetter))):
                raise CompileError((u"Duplicate method definition %s"), tag.range, this.name)
            # end if (line 303)
            if __x_cb(__x_cb(__x_cb(__cpm[this, "priv"]) and tag.isPublic) or (__x_cb(__cpm[this, "publ"]) and __x_not
(tag.isPublic))):
                raise ConflictError((u"A conflict exists with access modifier of definition %s"), tag.range, this.range, 
this.name)
            # end if (line 309)
            if __x_cb(__x_not(tag.isAccessor)):
                __cpm[this, "method"] = tag
            elif __x_cb(tag.isSetter):
                __cpm[this, "setter"] = tag
            else:
                __cpm[this, "getter"] = tag
            # end if (line 314)
            if __x_cb(tag.isPublic):
                __cpm[this, "publ"] = True
            else:
                __cpm[this, "priv"] = True
            # end if (line 321)
            __cpm[this, "verify"]()
        # end function __m_meetMethod (line 296)

        def __m_meetProperty(this, isPublic, range):
            if __x_cb(__x_cb(__x_cb(__x_cb(__cpm[this, "property"]) or __x_ne(__cpm[this, "method"], None)) or __x_ne(__cpm[this
, "setter"], None)) or __x_ne(__cpm[this, "getter"], None)):
                raise ConflictError((u"Incompatible override to property %s"), range, this.range, this.name)
            # end if (line 330)
            this.range = range
            __cpm[this, "property"] = True
            if __x_cb(isPublic):
                __cpm[this, "publ"] = True
            else:
                __cpm[this, "priv"] = True
            # end if (line 336)
            __cpm[this, "verify"]()
        # end function __m_meetProperty (line 329)

        def __m_toMethodName(this):
            __cpm[this, "verify"]()
            if __x_cb(this.isProperty):
                raise InternalError((u"property is not method"))
            # end if (line 346)
            if __x_cb(this.isMethod):
                return __cpm[this, "method"].toRawPython()
            # end if (line 349)
            g = __cpm[this, "getter"].toRawPython() if __x_cb(this.isGetter) else (u"None")
            s = __cpm[this, "setter"].toRawPython() if __x_cb(this.isSetter) else (u"None")
            return (u"__x_prop(") + g + (u", ") + s + (u")")
        # end function __m_toMethodName (line 344)

        def __m_verify(this):
            rsvdMember = StringMap()
            rsvdMember.sets([(u"__init__"), (u"__new__"), (u"__slots__"), (u"__dict__"), (u"__getattribute__"), (u"__getattr__"), 
(u"__setattr__"), (u"__delattr__"), (u"__instancecheck__"), (u"__subclasscheck__"), (u"__init_subclass__"), 
(u"__annotations__"), (u"__bases__"), (u"__cause__"), (u"__class__"), (u"__classcell__"), (u"__closure__"), 
(u"__code__"), (u"__context__"), (u"__debug__"), (u"__defaults__"), (u"__doc__"), (u"__file__"), (u"__future__"), 
(u"__globals__"), (u"__kwdefaults__"), (u"__mro__"), (u"__name__"), (u"__package__"), (u"__path__"), 
(u"__prepare__"), (u"__qualname__"), (u"__self__"), (u"__spec__"), (u"__traceback__")], True)
            rsvdStatic = StringMap()
            rsvdStatic.sets([(u"mro")], True)
            na = ArrayList(this.name)
            dupre = __x_cb(__x_cb(na.length >= 2) and __x_eq(na.get(0), (u"_"))) and __x_eq(na.get(1), (u"_"))
            dusuf = __x_cb(__x_cb(na.length >= 2) and __x_eq(na.get(-1), (u"_"))) and __x_eq(na.get(-2), (u"_"))
            if __x_cb(__x_cb(__x_cb(dupre) and dusuf) and (__x_cb(__x_cb(__x_eq(__cpm[this, "method"], None)) or __cpm[this
, "isStatic"]) or __x_not(__cpm[this, "publ"]))):
                raise CompileError((u"names starting and ending with double underscores in class statement are reserved for special method\
s"), this.range)
            # end if (line 370)
            if __x_cb(__x_cb(dupre) and __x_not(dusuf)):
                raise CompileError((u"names starting with double underscores in class statement are not allowed"), range)
            # end if (line 375)
            if __x_cb(__x_cb(__x_not(__cpm[this, "isStatic"])) and rsvdMember.has(this.name)):
                raise CompileError((u"class member ") + this.name + (u" is reserved"), range)
            # end if (line 378)
            if __x_cb(__x_cb(__cpm[this, "isStatic"]) and rsvdStatic.has(this.name)):
                raise CompileError((u"static member ") + this.name + (u" is reserved"), range)
            # end if (line 381)
            if __x_cb(__x_cb(__x_cb(__x_cb(__x_eq(__cpm[this, "getter"], None)) and __x_eq(__cpm[this, "setter"], 
None)) and __x_eq(__cpm[this, "method"], None)) and __x_not(__cpm[this, "property"])):
                raise InternalError((u"undefined class member"))
            # end if (line 384)
            if __x_cb(__x_cb(__x_not(__cpm[this, "priv"])) and __x_not(__cpm[this, "publ"])):
                raise InternalError((u"class member withput access modifier"))
            # end if (line 388)
        # end function __m_verify (line 357)

        def __m_ClassFieldDescriptor(this, name, isStatic):
            __csu(this, name, None)
            __cpm[this, "isStatic"] = isStatic
        # end function __m_ClassFieldDescriptor (line 393)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 398)

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            __cpm[this, "getter"] = None
            __cpm[this, "setter"] = None
            __cpm[this, "method"] = None
            __cpm[this, "property"] = False
            __cpm[this, "priv"] = False
            __cpm[this, "publ"] = False
            __cpm[this, "isStatic"] = False
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 404)

        __cpiT = __x_dpif("ClassFieldDescriptor", {"__slots__": ("getter", "isStatic", "method", "priv", "property"
, "publ", "setter"), "verify": __x_smet(__m_verify)})
        __clsT = __x_dcls("ClassFieldDescriptor", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "isAccessor": __x_prop(__g_isAccessor, None), "isGetter": __x_prop(__g_isGetter, None), "isMethod": __x_prop(__g_isMethod, None), 
"isPrivate": __x_prop(__g_isPrivate, None), "isProperty": __x_prop(__g_isProperty, None), "isSetter": __x_prop(__g_isSetter, None), 
"meetMethod": __m_meetMethod, "meetProperty": __m_meetProperty, "toMethodName": __m_toMethodName, "__init__": __m_ClassFieldDescriptor})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory ClassFieldDescriptor, __c_ClassFieldDescriptor (line 265)

    def __c_LocalVar(__cexT):
        def __g_isSpecial(this):
            if __x_cb(__x_cb(__x_cb(StrTool.strlen(this.name) > 2) and __x_eq(StrTool.codePointAt(this.name, 0), 
95)) and __x_eq(StrTool.codePointAt(this.name, 0), 95)):
                return True
            # end if (line 431)
            return (super(__clsT, this)).isSpecial
        # end function __g_isSpecial (line 430)

        def __m_redeclare(this, __v_from, range = (None)):
            (super(__clsT, this)).redeclare(__v_from, range)
        # end function __m_redeclare (line 438)

        def __m_read(this, __v_from, range = (None)):
            pass
        # end function __m_read (line 442)

        def __m_write(this, __v_from, range = (None)):
            this.assigned = True
            if __x_cb(__x_ne(__v_from, this.at)):
                this.closure = True
            # end if (line 448)
        # end function __m_write (line 446)

        def __m_toRawPython(this):
            if __x_cb(this.closure):
                return (u"__u_") + this.encode()
            # end if (line 454)
            return this.toOriginPython()
        # end function __m_toRawPython (line 453)

        def __m_toPython(this):
            clsuf = (u".val") if __x_cb(this.closure) else (u"")
            return this.toRawPython() + clsuf
        # end function __m_toPython (line 460)

        def __m_toOriginPython(this):
            if __x_cb(__x_not(this.isSpecial)):
                return this.name
            # end if (line 466)
            return (u"__v_") + this.encode()
        # end function __m_toOriginPython (line 465)

        def __m_toString(this):
            n = this.name
            return (u"local.") + ((u"?") if __x_cb(__x_eq(n, None)) else n) + ((u"@closure") if __x_cb(this.closure)
 else (u""))
        # end function __m_toString (line 472)

        def __m_LocalVar(this, name, at, range):
            __csu(this, name, at, range)
        # end function __m_LocalVar (line 478)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 482)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 488)

        __clsT = __x_dcls("LocalVar", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "isSpecial": __x_prop(__g_isSpecial, None), 
"read": __m_read, "redeclare": __m_redeclare, "toOriginPython": __m_toOriginPython, "toPython": __m_toPython, 
"toRawPython": __m_toRawPython, "toString": __m_toString, "write": __m_write, "__init__": __m_LocalVar})
        return __clsT
    # end class factory LocalVar, __c_LocalVar (line 429)

    def __c_ClassTag(__cexT):
        def __m_redeclare(this, __v_from, range = (None)):
            raise ConflictError((u"Duplicate class definition"), range, this.range)
        # end function __m_redeclare (line 501)

        def __m_write(this, __v_from, range = (None)):
            raise ConflictError((u"Illegal assignment to class definition"), range, this.range)
        # end function __m_write (line 505)

        def __m_toPython(this):
            return this.toRawPython()
        # end function __m_toPython (line 509)

        def __m_toString(this):
            n = this.name
            f = this.at
            return (u"class.") + ((u"?") if __x_cb(__x_eq(n, None)) else n) + ((u"") if __x_cb(__x_eq(f, None)) else 
(u"[") + this.at.functionToken + (u"]"))
        # end function __m_toString (line 513)

        def __m_toFactoryName(this):
            return (u"__c_") + this.encode()
        # end function __m_toFactoryName (line 520)

        def __m_ClassTag(this, name, target, range):
            __csu(this, name, target, range)
            this.assigned = True
        # end function __m_ClassTag (line 524)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 529)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 535)

        __clsT = __x_dcls("ClassTag", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "redeclare": __m_redeclare, 
"toFactoryName": __m_toFactoryName, "toPython": __m_toPython, "toString": __m_toString, "write": __m_write, 
"__init__": __m_ClassTag})
        return __clsT
    # end class factory ClassTag, __c_ClassTag (line 500)

    def __c_FunctionTag(__cexT):
        def __m_read(this, __v_from, range = (None)):
            pass
        # end function __m_read (line 548)

        def __m_redeclare(this, __v_from, range = (None)):
            raise ConflictError((u"Duplicate function definition"), range, this.range)
        # end function __m_redeclare (line 552)

        def __m_write(this, __v_from, range = (None)):
            raise ConflictError((u"Illegal assignment to function definition"), range, this.range)
        # end function __m_write (line 556)

        def __m_toPython(this):
            return this.toRawPython()
        # end function __m_toPython (line 560)

        def __m_toString(this):
            n = this.name
            f = this.at
            return (u"def.") + ((u"?") if __x_cb(__x_eq(n, None)) else n) + ((u"") if __x_cb(__x_eq(f, None)) else 
(u"[") + this.at.functionToken + (u"]"))
        # end function __m_toString (line 564)

        def __m_FunctionTag(this, name, target, range):
            __csu(this, name, target, range)
            this.assigned = True
        # end function __m_FunctionTag (line 571)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 576)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 582)

        __clsT = __x_dcls("FunctionTag", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "read": __m_read, 
"redeclare": __m_redeclare, "toPython": __m_toPython, "toString": __m_toString, "write": __m_write, "__init__": __m_FunctionTag})
        return __clsT
    # end class factory FunctionTag, __c_FunctionTag (line 547)

    def __c_FunctionExpTag(__cexT):
        def __m_write(this, __v_from, range = (None)):
            raise ConflictError((u"Illegal assignment to function expression"), range, this.range)
        # end function __m_write (line 594)

        def __m_toRawPython(this):
            n = this.name
            s = (u"__f") + this.at.functionToken + (u"_")
            return s if __x_cb(__x_eq(n, None)) else s + this.encode()
        # end function __m_toRawPython (line 598)

        def __m_toComment(this):
            n = this.name
            s = this.toRawPython()
            if __x_cb(__x_eq(n, None)):
                n = (u"<anonymous>")
            # end if (line 607)
            return n + (u" (") + s + (u")")
        # end function __m_toComment (line 604)

        def __m_FunctionExpTag(this, name, target, range):
            __csu(this, name, target, range)
        # end function __m_FunctionExpTag (line 613)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 617)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 623)

        __clsT = __x_dcls("FunctionExpTag", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "toComment": __m_toComment, 
"toRawPython": __m_toRawPython, "write": __m_write, "__init__": __m_FunctionExpTag})
        return __clsT
    # end class factory FunctionExpTag, __c_FunctionExpTag (line 593)

    def __c_GlobalVar(__cexT):
        def __m_redeclare(this, __v_from, range = (None)):
            raise InternalError((u"redeclare GlobalVar"))
        # end function __m_redeclare (line 635)

        def __m_read(this, __v_from, range = (None)):
            pass
        # end function __m_read (line 639)

        def __m_write(this, __v_from, range = (None)):
            raise InternalError((u"Illegal assignment to superglobal variables"))
        # end function __m_write (line 643)

        def __m_toRawPython(this):
            return this.name
        # end function __m_toRawPython (line 647)

        def __m_toString(this):
            n = this.name
            return (u"global.") + ((u"?") if __x_cb(__x_eq(n, None)) else n)
        # end function __m_toString (line 651)

        def __m_GlobalVar(this, name):
            __csu(this, name, None, None)
            this.assigned = True
        # end function __m_GlobalVar (line 656)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 661)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 667)

        __clsT = __x_dcls("GlobalVar", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "read": __m_read, 
"redeclare": __m_redeclare, "toRawPython": __m_toRawPython, "toString": __m_toString, "write": __m_write, 
"__init__": __m_GlobalVar})
        return __clsT
    # end class factory GlobalVar, __c_GlobalVar (line 634)

    def __c_MethodTag(__cexT):
        def __m_read(this, __v_from, range = (None)):
            pass
        # end function __m_read (line 680)

        def __m_redeclare(this, __v_from, range = (None)):
            raise InternalError((u"declaration of method tag"))
        # end function __m_redeclare (line 684)

        def __m_toRawPython(this):
            pf = (((u"t") if __x_cb(this.isSetter) else (u"h")) if __x_cb(this.isAccessor) else (u"n")) if __x_cb\
(this.isStatic) else (((u"s") if __x_cb(this.isSetter) else (u"g")) if __x_cb(this.isAccessor) else (u"m")
)
            return (u"__") + pf + (u"_") + this.encode()
        # end function __m_toRawPython (line 688)

        def __m_toString(this):
            n = this.name
            return ((u"public.") if __x_cb(this.isPublic) else (u"private.")) + ((u"static.") if __x_cb(this.isStatic)
 else (u"")) + (((u"setter") if __x_cb(this.isSetter) else (u"getter")) if __x_cb(this.isAccessor) else 
(u"method")) + (u".") + ((u"?") if __x_cb(__x_eq(n, None)) else n)
        # end function __m_toString (line 695)

        def __m_MethodTag(this, name, methodType, isStatic, isPublic, target, range):
            __csu(this, name, target, range)
            am = StringMap([[(u"method"), False], [(u"get"), True], [(u"set"), True]])
            this.isAccessor = am.get(methodType)
            this.isSetter = __x_eq(methodType, (u"set"))
            this.isStatic = isStatic
            this.isPublic = isPublic
        # end function __m_MethodTag (line 702)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 711)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 717)

        __clsT = __x_dcls("MethodTag", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": ("isAccessor", 
"isPublic", "isSetter", "isStatic"), "read": __m_read, "redeclare": __m_redeclare, "toRawPython": __m_toRawPython, 
"toString": __m_toString, "__init__": __m_MethodTag})
        return __clsT
    # end class factory MethodTag, __c_MethodTag (line 679)

    def __c_TempVar(__cexT):
        def __m_toRawPython(this):
            return (u"__r") + Identifier.encodeRadix32(this.index)
        # end function __m_toRawPython (line 730)

        def __m_toString(this):
            return (u"temp[") + StrTool.str(this.index) + (u"]")
        # end function __m_toString (line 734)

        def __m_TempVar(this, index, at):
            __csu(this, None, at, None)
            this.assigned = True
            this.index = index
        # end function __m_TempVar (line 738)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 744)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 750)

        __clsT = __x_dcls("TempVar", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": ("index",), 
"toRawPython": __m_toRawPython, "toString": __m_toString, "__init__": __m_TempVar})
        return __clsT
    # end class factory TempVar, __c_TempVar (line 729)

    __r0 = __x_imp((u".compat"))
    ArrayList = __r0.ArrayList
    StrTool = __r0.StrTool
    printf = __r0.printf
    __r1 = __x_imp((u".StringMap"))
    StringMap = __r1.StringMap
    __r2 = __x_imp((u".utils"))
    CompileError = __r2.CompileError
    ElementPattern = __r2.ElementPattern
    Range = __r2.Range
    ConflictError = __r2.ConflictError
    InternalError = __r2.InternalError
    XMLDumper = __r2.XMLDumper
    Identifier = __c_Identifier()
    Identifier.pythonKeywords.sets(ArrayList([(u"False"), (u"None"), (u"True"), (u"and"), (u"as"), (u"assert"), 
(u"async"), (u"await"), (u"break"), (u"class"), (u"continue"), (u"def"), (u"del"), (u"elif"), (u"else"), 
(u"except"), (u"finally"), (u"for"), (u"from"), (u"global"), (u"if"), (u"import"), (u"in"), (u"is"), 
(u"lambda"), (u"nonlocal"), (u"not"), (u"or"), (u"pass"), (u"raise"), (u"return"), (u"try"), (u"while"), 
(u"with"), (u"yield"), (u"exec")]), True)
    Attribute = __c_Attribute(Identifier)
    Variable = __c_Variable(Identifier)
    BuiltinVar = __c_BuiltinVar(Variable)
    ClassFieldDescriptor = __c_ClassFieldDescriptor(Attribute)
    LocalVar = __c_LocalVar(Variable)
    ClassTag = __c_ClassTag(LocalVar)
    FunctionTag = __c_FunctionTag(LocalVar)
    FunctionExpTag = __c_FunctionExpTag(FunctionTag)
    GlobalVar = __c_GlobalVar(Variable)
    MethodTag = __c_MethodTag(FunctionTag)
    TempVar = __c_TempVar(Variable)
# program end


__()
