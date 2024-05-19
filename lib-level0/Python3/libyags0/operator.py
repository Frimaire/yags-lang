# -*- coding: utf-8 -*-
# operators of YAGS runtime
from __future__ import print_function, absolute_import, division, generators, unicode_literals
from .compat import IntegerTypes, NumberTypes, StringType, BytesType


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
    if isinstance(x, NumberTypes):
        return 'number'
    if isinstance(x, StringType):
        return 'string'
    if isinstance(x, BytesType):
        return 'string'
    if isinstance(x, complex):
        return 'complex'
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
