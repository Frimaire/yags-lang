# -*- coding: utf-8 -*-
# operators of YAGS runtime
from __future__ import print_function, absolute_import, division, generators, unicode_literals
from .compat import IntegerTypes, NumberTypes, StringType, BytesType
from numbers import Complex, Real


# operator "==="
def strictEqual(x, y):
    # in python, Boolean is integer!
    if True is x:
        return True is y
    if False is x:
        return False is y
    if isinstance(x, IntegerTypes):
        if isinstance(y, IntegerTypes):
            return x == y
        return False
    if isinstance(x, float):
        if isinstance(y, float):
            return x == y
        return False
    if isinstance(x, complex):
        if isinstance(y, complex):
            return x == y
        return False
    if isinstance(x, StringType):
        if isinstance(y, StringType):
            return x == y
        elif isinstance(y, BytesType):
            # compare "binary string"
            if len(x) != len(y):
                return False
            l = len(x)
            i = 0
            while i < l:
                if not ord(x[i]) == ord(y[i]):
                    return False
                i = i + 1
            return True
        return False
    # treat bytes a "string"
    if isinstance(x, BytesType):
        if isinstance(y, BytesType):
            return x == y
        if isinstance(y, StringType):
            # compare "binary string"
            if len(x) != len(y):
                return False
            l = len(x)
            i = 0
            while i < l:
                if not ord(x[i]) == ord(y[i]):
                    return False
                i = i + 1
            return True
        return False
    # Tuple
    # https://github.com/tc39/proposal-record-tuple
    # In ES, tuple is deeply immutable whose members are limited to primitives
    # but YAGS does not as what Python does.
    # null is in this case
    if isinstance(x, tuple):
        if isinstance(y, tuple):
            if len(x) != len(y):
                return False
            l = len(x)
            i = 0
            while i < l:
                if not strictEqual(x[i], y[i]):
                    return False
                i = i + 1
            return True
        return False
    return x is y
# end strictEqual


# operator "!=="
# actually, this is "not strictly equal"
def strictInequal(x, y):
    return not strictEqual(x, y)
# end strictInequal


# operator typeof
def typeof(x):
    if isinstance(x, bool):
        return 'boolean'
    if isinstance(x, Real):
        return 'number'
    if isinstance(x, Complex):
        return 'complex'
    if isinstance(x, StringType):
        return 'string'
    if isinstance(x, BytesType):
        return 'string'
    if callable(x):
        return 'function'
    return 'object'
# end typeof


# check if x is boolean for logic operators
def coerceBoolean(x):
    if True is x:
        return x
    if False is x:
        return x
    raise TypeError('Cannot convert an Object to a Boolean, use explicit comparisons')
# end coerceBoolean


# check if x is boolean for logic not operator
def coerceNot(x):
    if True is x:
        return False
    if False is x:
        return True
    raise TypeError('Cannot convert an Object to a Boolean, use explicit comparisons')
# end coerceNot


# implicit conversion to boolean
def toBoolean(x):
    if True is x:
        return True
    if False is x:
        return False
    T = type(x)
    try:
        bf = type.__getattribute__(T, '__bool__')
    except AttributeError:
        return True
    if not callable(bf):
        raise TypeError('__bool__ method of ' + type.__getattribute__(T, '__name__') +
                        ' is not callable')
    r = bf(x)
    if True is r:
        return True
    if False is r:
        return False
    raise TypeError('__bool__ must return a boolean')
# end toBoolean


# implicit conversion to boolean and invert
def toNotBoolean(x):
    if True is x:
        return False
    if False is x:
        return True
    T = type(x)
    try:
        bf = type.__getattribute__(T, '__bool__')
    except AttributeError:
        return False
    if not callable(bf):
        raise TypeError('__bool__ method of ' + type.__getattribute__(T, '__name__') +
                        ' is not callable')
    r = bf(x)
    if True is r:
        return False
    if False is r:
        return True
    raise TypeError('__bool__ must return a boolean')
# end toNotBoolean


# check if x is number for ++
def inc(x):
    if isinstance(x, NumberTypes) and not isinstance(x, bool):
        return x + 1
    raise TypeError('update operator can only be used with real number')
# end inc


# check if x is number for --
def dec(x):
    if isinstance(x, NumberTypes) and not isinstance(x, bool):
        return x - 1
    raise TypeError('update operator can only be used with real number')
# end inc


# operator "instanceof"
def instanceof(self, cls):
    if isinstance(cls, tuple):
        raise TypeError('Right-hand side of \'instanceof\' is not a class')
    return isinstance(self, cls)
# end instanceof
