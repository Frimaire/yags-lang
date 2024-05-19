# -*- coding: utf-8 -*-
# tools for private fields
# Private fields are stored on a WeakMap, just like what Babel does.
from __future__ import print_function, absolute_import, division, generators
from weakref import ref
from .function import bindThis


# same value wrapper for finding the reference (used for key)
class Referer(object):
    __slots__ = ('object',)

    def __hash__(self):
        return id(self.object)
    # end hash

    # __eq__ is implemented by WeakRef
    def __eq__(self, obj):
        return NotImplemented

    # __ne__ is implemented by WeakRef
    def __ne__(self, obj):
        return NotImplemented

    def __init__(self, object):
        self.object = object
    # end __init__
# end Referer


# wrapper of weakref
class WeakRef(ref):
    __slots__ = ('origid',)

    def __hash__(self):
        return self.origid
    # end hash

    # make the object samevalue with its ref
    def __eq__(self, obj):
        if isinstance(obj, WeakRef):
            return obj is self
        elif isinstance(obj, Referer):
            return obj.object is self()
        return False
    # end __eq__

    def __ne__(self, obj):
        if isinstance(obj, WeakRef):
            return obj is not self
        elif isinstance(obj, Referer):
            return obj.object is not self()
        return True
    # end __ne__

    def __init__(self, obj, cb):
        super(WeakRef, self).__init__(obj, cb)
        self.origid = id(obj)
    # end __init__
# end WeakRef


# the WeakMap to store the private fields
# redirect the private fields to Fields
class PrivateMap(object):
    __slots__ = ('refMap', 'theClass', 'Fields')

    # create a private field and return it
    def create(self, obj):
        m = self.refMap
        r = WeakRef(obj, self.gc)
        f = self.Fields()
        m[r] = f
        return f
    # end create

    # destory the reference, called when GC
    def gc(self, r):
        del self.refMap[r]
    # end gc

    # set the private attribute
    # use the form of pm[obj, attr]
    def __setitem__(self, o, val):
        (obj, attr) = o
        m = self.refMap
        ro = Referer(obj)
        pf = m.get(ro, None)
        if pf is None:
            setattr(obj, attr, val)
            return
        # for private setter, this should be bound to the original this
        accessor = getattr(self.Fields, attr)
        if isinstance(accessor, property):
            accessor.__set__(obj, val)
            return
        # for private methods, an error will be thrown here
        setattr(pf, attr, val)
    # end setAttr

    # get the private attribute
    # use the form of pm[obj, attr]
    def __getitem__(self, o):
        (obj, attr) = o
        m = self.refMap
        ro = Referer(obj)
        pf = m.get(ro, None)
        if pf is None:
            return getattr(obj, attr)
        accessor = getattr(self.Fields, attr)
        if isinstance(accessor, property):
            # for private getter, this should be bound to the original this
            return accessor.__get__(obj)
        elif callable(accessor):
            # for private method, bind the this pointer
            # NOTE: staticmethod should be used, otherwise a TypeError will be thrown in py2
            return bindThis(accessor, obj)
        # property (member_descriptor) is not callable
        return getattr(pf, attr)
    # end getAttr

    # delete the private attribute
    # use the form of pm[obj, attr]
    def __delitem__(self, o):
        (obj, attr) = o
        m = self.refMap
        ro = Referer(obj)
        if ro not in m:
            return delattr(obj, attr)
        # private fields is not configurable
        raise TypeError("Cannot delete property '" + attr + "'")
    # end getAttr

    def __init__(self, theClass, Fields):
        self.theClass = theClass
        self.Fields = Fields
        self.refMap = {}
    # end __init__
# end PrivateMap


# redirect the class private properties
class StaticPrivateGate(object):
    __slots__ = ('theClass', 'fields')

    # set the private attribute
    # use the form of Class[obj, attr]
    def __setitem__(self, o, val):
        (obj, attr) = o
        if obj is self.theClass:
            return setattr(self.fields, attr, val)
        return setattr(obj, attr, val)
    # end __setitem__

    # get the private attribute
    # use the form of pm[obj, attr]
    def __getitem__(self, o):
        (obj, attr) = o
        if obj is self.theClass:
            return getattr(self.fields, attr)
        return getattr(obj, attr)
    # end __getitem__

    # delete the private attribute
    # use the form of pm[obj, attr]
    def __delitem__(self, o):
        (obj, attr) = o
        if obj is self.theClass:
            # private fields is not configurable
            raise TypeError("Cannot delete property '" + attr + "'")
        return delattr(obj, attr)
    # end __delitem__

    # here the fields is the (only one) instance of Fields
    def __init__(self, theClass, fields):
        self.theClass = theClass
        self.fields = fields
    # end __init__
# end StaticPrivateGate


# redirect the class/instance private properties
# use this class if a member name is both static private and instance private
class ClassPrivateGate(object):
    __slots__ = ('theClass', 'theMap', 'fields')

    # set the private attribute
    # use the form of Class[obj, attr]
    def __setitem__(self, o, val):
        (obj, attr) = o
        if obj is self.theClass:
            return setattr(self.fields, attr, val)
        return self.theMap.__setitem__(o, val)
    # end __setitem__

    # get the private attribute
    # use the form of pm[obj, attr]
    def __getitem__(self, o):
        (obj, attr) = o
        if obj is self.theClass:
            return getattr(self.fields, attr)
        return self.theMap.__getitem__(o)
    # end __getitem__

    # delete the private attribute
    # use the form of pm[obj, attr]
    def __delitem__(self, o):
        (obj, attr) = o
        if obj is self.theClass:
            # private fields is not configurable
            raise TypeError("Cannot delete property '" + attr + "'")
        return self.theMap.__delitem__(o)
    # end __delitem__

    # here the fields is the (only one) instance of Fields
    def __init__(self, theClass, theMap, fields):
        self.theClass = theClass
        self.theMap = theMap
        self.fields = fields
    # end __init__
# end ClassPrivateGate


# the WeakMap to store the static fields
# redirect the static fields to staticFields
class StaticMap(object):
    __slots__ = ('refMap',)

    # create a static field and register it
    def create(self, clsT, StaticField):
        m = self.refMap
        r = WeakRef(clsT, self.gc)
        f = StaticField()
        m[r] = f
        return f
    # end create

    # destory the reference, called when GC
    def gc(self, r):
        del self.refMap[r]
    # end gc

    # get the static field
    def __getitem__(self, clsT):
        m = self.refMap
        r = Referer(clsT)
        return m[r]
    # end getClass

    def __init__(self):
        self.refMap = {}
    # end __init__
# end StaticMap


_staticFields = StaticMap()


# the base meta class
class Class(type):
    __slots__ = ()

    def __getattribute__(clsT, name):
        if (name == 'mro' or name[0:2] == '__' and name[-2:] == '__'):
            return type.__getattribute__(clsT, name)
        return getattr(_staticFields[clsT], name)
    # end __getattribute__

    def __setattr__(clsT, name, value):
        if (name == 'mro' or name[0:2] == '__' and name[-2:] == '__'):
            return type.__setattr__(clsT, name)
        return setattr(_staticFields[clsT], name, value)
    # end __setattr__

    # __delattr__
    def __delattr__(self, clsT, name):
        # Class object is always sealed
        # Python throws AttributeError instead of TypeError
        raise AttributeError('Cannot delete property ' + name + ' of class object')
    # end __delattr__

    def __init__(clsT, *a):
        type.__init__(clsT, *a)
    # end __init__
# end class Class


# define class
# @param {str} name, the name of the class
# @param {type} Super, the super class
# @param {dict} staticField, a set of key-value pairs for static fields
# @param {dict} instanceField, a set of key-value pairs for instance fields
#               (including __init__)
def defineClass(name, Super, staticField, instanceField):
    if not isinstance(Super, type):
        raise TypeError('Class extends value is not a type object')

    # static members
    _StaticClass = type('_StaticField_' + name, (object,), staticField)

    # if Super instanceof YAGS's Class, __weakref__ already existed in the __slots__
    if not (isinstance(Super, Class) or hasattr(Super, '__weakref__')):
        instanceField['__slots__'] = instanceField['__slots__'] + ('__weakref__',)
    # end if

    # the class
    clsT = Class(name, (Super,), instanceField)
    _staticFields.create(clsT, _StaticClass)

    return clsT
# end defineClass


# define private fields for instance members
# @param {str} name, the name of the class
# @param {dict} fields, a set of key-value pairs for fields
def definePrivateInstanceField(name, fields):
    return type('Private_' + name, (object,), fields)
# end definePrivateInstanceField


# define private fields for static members
# @param {str} name, the name of the class
# @param {dict} fields, a set of key-value pairs for fields
def definePrivateStaticField(name, fields):
    return type('Private_Static_' + name, (object,), fields)
# end definePrivateStaticField


