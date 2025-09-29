# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, division, generators

__all__ = ("Attribute", "BaseAttribute", "ClassFieldDescriptor", "isKeyword", "isSpecial")


def __():
    from libyags0 import __x_tup, __x_tupof, __x_lst, __x_errT, __x_eq, __x_ne, __x_typ, __x_cb, __x_not, __x_iof, __x_inc, __x_dec, __x_var, __x_imf, __x_at_take, __x_at_drop, __x_at_forEach, __x_at_map, __x_at_filter, __x_at_flatMap, __x_at_some, __x_at_every, __x_at_find, __x_at_findIndex, __x_at_reduce, __x_at_join, __x_at_bind, __x_at_apply, __x_at_length, __x_at_isEmpty, __x_at_push, __x_at_pop, __x_at_shift, __x_at_unshift, __x_at_slice, __x_at_splice, __x_at_has, __x_dcls, __x_dpif, __x_dpsf, __x_prmT, __x_csgT, __x_cpgT, __x_objT, __x_smet, __x_prop, __x_tob, __x_tnb, Infinity, NaN
    __x_imp = __x_imf(__name__)
    global Attribute, BaseAttribute, ClassFieldDescriptor, isKeyword, isSpecial

    # function definitions:

    def isKeyword(name):
        return pythonKeywords.has(name)
    # end function isKeyword

    def isSpecial(name):
        def __f3_(c, k, a):
            ch = StrTool.codePointAt(c)
            if __x_cb(__x_eq(ch, 36)):
                __u_enc.val = True
                return False
            # end if
            if __x_cb(ch >= 128):
                __u_enc.val = True
                return False
            # end if
        # end function <anonymous> (__f3_)

        __u_enc = __x_var()
        __u_enc.val = False
        ars = ArrayList(name)
        ars.forEach(__f3_)
        return __u_enc.val
    # end function isSpecial

    # class definitions:

    def __c_BaseAttribute():
        def __m_____str____(this):
            return this.toString()
        # end function __str__(__m_____str____)

        def __m_toString(this):
            return this.name
        # end function __m_toString

        def __m_BaseAttribute(this, name, range):
            __csu(this)
            this.name = name
            this.range = range
        # end function __m_BaseAttribute

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

        __clsT = __x_dcls("BaseAttribute", __x_objT, {"__slots__": (), "__init__": __csi}, {"__slots__": ("name", 
"range"), "__str__": __m_____str____, "toString": __m_toString, "__init__": __m_BaseAttribute})
        return __clsT
    # end class factory BaseAttribute, __c_BaseAttribute

    def __c_Attribute(__cexT):
        def __m_toPython(this):
            return this.name
        # end function __m_toPython

        def __m_Attribute(this, name, range):
            __csu(this, name, range)
            if __x_cb(isSpecial(name)):
                CAS.error(range, (u"Attribute name with $ or non-ASCII characters is not allowed: %s"), name)
            # end if
            if __x_cb(isKeyword(name)):
                CAS.error(range, (u"Python keyword cannot be used as attribute: %s"), name)
            # end if
        # end function __m_Attribute

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

        __clsT = __x_dcls("Attribute", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "toPython": __m_toPython, 
"__init__": __m_Attribute})
        return __clsT
    # end class factory Attribute, __c_Attribute

    def __c_ClassFieldDescriptor(__cexT):
        def __g_isProperty(this):
            __cpm[this, "verify"]()
            return __cpm[this, "property"]
        # end function __g_isProperty

        def __g_isAccessor(this):
            __cpm[this, "verify"]()
            return __x_cb(__x_ne(__cpm[this, "getter"], None)) or __x_ne(__cpm[this, "setter"], None)
        # end function __g_isAccessor

        def __g_isGetter(this):
            __cpm[this, "verify"]()
            return __x_ne(__cpm[this, "getter"], None)
        # end function __g_isGetter

        def __g_isSetter(this):
            __cpm[this, "verify"]()
            return __x_ne(__cpm[this, "setter"], None)
        # end function __g_isSetter

        def __g_isMethod(this):
            __cpm[this, "verify"]()
            return __x_ne(__cpm[this, "method"], None)
        # end function __g_isMethod

        def __g_isPrivate(this):
            __cpm[this, "verify"]()
            return __cpm[this, "priv"]
        # end function __g_isPrivate

        def __m_meetMethod(this, tag):
            if __x_cb(__x_ne(__cpm[tag, "isStatic"], __cpm[this, "isStatic"])):
                raise InternalError((u"mismatched static flag"))
            # end if
            if __x_cb(__cpm[this, "property"]):
                CAS.delayedError(tag.range, (u"Incompatible override to property %s"), this.name)
                CAS.note(this.range, (u"'%s' has previously defined here."), this.name)
            # end if
            if __x_cb(__x_cb(__x_cb(__x_cb(__x_ne(__cpm[this, "method"], None)) or (__x_cb(__x_cb(__x_ne(__cpm[this
, "setter"], None)) or __x_ne(__cpm[this, "getter"], None)) and __x_not(tag.isAccessor))) or (__x_cb(__x_ne(__cpm[this
, "setter"], None)) and tag.isSetter)) or (__x_cb(__x_ne(__cpm[this, "getter"], None)) and __x_not(tag\
.isSetter))):
                CAS.error(tag.range, (u"Duplicate method definition %s"), this.name)
            # end if
            if __x_cb(__x_cb(__x_cb(__cpm[this, "priv"]) and tag.isPublic) or (__x_cb(__cpm[this, "publ"]) and __x_not
(tag.isPublic))):
                CAS.delayedError(tag.range, (u"A conflict exists with access modifier of definition %s"), this.name)
                CAS.note(this.range, (u"'%s' has previously defined here."), this.name)
            # end if
            if __x_cb(__x_not(tag.isAccessor)):
                __cpm[this, "method"] = tag
            elif __x_cb(tag.isSetter):
                __cpm[this, "setter"] = tag
            else:
                __cpm[this, "getter"] = tag
            # end if
            if __x_cb(tag.isPublic):
                __cpm[this, "publ"] = True
            else:
                __cpm[this, "priv"] = True
            # end if
            __cpm[this, "verify"]()
        # end function __m_meetMethod

        def __m_meetProperty(this, isPublic, range):
            if __x_cb(__x_cb(__x_cb(__x_cb(__cpm[this, "property"]) or __x_ne(__cpm[this, "method"], None)) or __x_ne(__cpm[this
, "setter"], None)) or __x_ne(__cpm[this, "getter"], None)):
                CAS.delayedError(range, (u"Incompatible override to property %s"), this.name)
                CAS.note(this.range, (u"'%s' has previously declared here."), this.name)
            # end if
            this.range = range
            __cpm[this, "property"] = True
            if __x_cb(isPublic):
                __cpm[this, "publ"] = True
            else:
                __cpm[this, "priv"] = True
            # end if
            __cpm[this, "verify"]()
        # end function __m_meetProperty

        def __m_toMethodName(this):
            __cpm[this, "verify"]()
            if __x_cb(this.isProperty):
                raise InternalError((u"property is not method"))
            # end if
            if __x_cb(this.isMethod):
                return __cpm[this, "method"].toRawPython()
            # end if
            g = __cpm[this, "getter"].toRawPython() if __x_cb(this.isGetter) else (u"None")
            s = __cpm[this, "setter"].toRawPython() if __x_cb(this.isSetter) else (u"None")
            return (u"__x_prop(") + g + (u", ") + s + (u")")
        # end function __m_toMethodName

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
                CAS.error(this.range, (u"names starting and ending with double underscores in class statement are reserved for special method\
s"))
            # end if
            if __x_cb(__x_cb(dupre) and __x_not(dusuf)):
                CAS.error(range, (u"names starting with double underscores in class statement are not allowed"))
            # end if
            if __x_cb(__x_cb(__x_not(__cpm[this, "isStatic"])) and rsvdMember.has(this.name)):
                CAS.error(range, (u"class member %s is reserved"), this.name)
            # end if
            if __x_cb(__x_cb(__cpm[this, "isStatic"]) and rsvdStatic.has(this.name)):
                CAS.error(range, (u"static member %s is reserved"), this.name)
            # end if
            if __x_cb(__x_cb(__x_cb(__x_cb(__x_eq(__cpm[this, "getter"], None)) and __x_eq(__cpm[this, "setter"], 
None)) and __x_eq(__cpm[this, "method"], None)) and __x_not(__cpm[this, "property"])):
                raise InternalError((u"undefined class member"))
            # end if
            if __x_cb(__x_cb(__x_not(__cpm[this, "priv"])) and __x_not(__cpm[this, "publ"])):
                raise InternalError((u"class member withput access modifier"))
            # end if
        # end function __m_verify

        def __m_ClassFieldDescriptor(this, name, range, isStatic):
            __csu(this, name, range)
            __cpm[this, "isStatic"] = isStatic
        # end function __m_ClassFieldDescriptor

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

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
        # end instance initializer and super constructor __csu

        __cpiT = __x_dpif("ClassFieldDescriptor", {"__slots__": ("getter", "isStatic", "method", "priv", "property"
, "publ", "setter"), "verify": __x_smet(__m_verify)})
        __clsT = __x_dcls("ClassFieldDescriptor", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "isAccessor": __x_prop(__g_isAccessor, None), "isGetter": __x_prop(__g_isGetter, None), "isMethod": __x_prop(__g_isMethod, None), 
"isPrivate": __x_prop(__g_isPrivate, None), "isProperty": __x_prop(__g_isProperty, None), "isSetter": __x_prop(__g_isSetter, None), 
"meetMethod": __m_meetMethod, "meetProperty": __m_meetProperty, "toMethodName": __m_toMethodName, "__init__": __m_ClassFieldDescriptor})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory ClassFieldDescriptor, __c_ClassFieldDescriptor

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
    pythonKeywords = StringMap()
    pythonKeywords.sets(ArrayList([(u"False"), (u"None"), (u"True"), (u"and"), (u"as"), (u"assert"), (u"async"), 
(u"await"), (u"break"), (u"class"), (u"continue"), (u"def"), (u"del"), (u"elif"), (u"else"), (u"except"), 
(u"finally"), (u"for"), (u"from"), (u"global"), (u"if"), (u"import"), (u"in"), (u"is"), (u"lambda"), 
(u"nonlocal"), (u"not"), (u"or"), (u"pass"), (u"raise"), (u"return"), (u"try"), (u"while"), (u"with"), 
(u"yield"), (u"exec")]), True)
    BaseAttribute = __c_BaseAttribute()
    Attribute = __c_Attribute(BaseAttribute)
    ClassFieldDescriptor = __c_ClassFieldDescriptor(Attribute)
# program end


__()
