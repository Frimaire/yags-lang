# -*- coding: utf-8 -*-
# container utils of YAGS runtime for python 2
from __future__ import print_function, absolute_import, division, generators

from .compat import IntegerTypes, NumberTypes, LongType
from .compat import NEG_SAFE_FLOAT, POS_SAFE_FLOAT, isInf, Infinity
from .compat import RangeError
from .compat import ISPY2

if ISPY2:
    from collections import MutableSequence
else:
    from collections.abc import MutableSequence
# end if


# integer or safe number can be index
def qualifyIndex(x, name='index'):
    if isinstance(x, bool) or not isinstance(x, NumberTypes):
        raise TypeError("'" + type(x).__name__ + "' cannot be used as an " + name)
    if isinstance(x, IntegerTypes):
        return x
    if not (x <= POS_SAFE_FLOAT and x >= NEG_SAFE_FLOAT):
        raise RangeError('Invalid ' + name)
    xi = LongType(x)
    if xi != x:
        raise RangeError('Invalid ' + name)
    return xi
# end qualifyIndex


# integer or safe number can be index
def qualifyIndexAllowInfinity(x, name):
    if isinstance(x, bool) or not isinstance(x, NumberTypes):
        raise TypeError("'" + type(x).__name__ + "' cannot be used as an " + name)
    if isinstance(x, IntegerTypes):
        return x
    if isInf(x):
        return x
    if not (x <= POS_SAFE_FLOAT and x >= NEG_SAFE_FLOAT):
        raise RangeError('Invalid ' + name)
    xi = LongType(x)
    if xi != x:
        raise RangeError('Invalid ' + name)
    return xi
# end qualifyIndex


# like qualifyIndex but x should be grater or equal than zero
def qualifyNaturalIndex(x, name='index'):
    if isinstance(x, bool) or not isinstance(x, NumberTypes):
        raise TypeError("'" + type(x).__name__ + "' cannot be used as an " + name)
    if x < 0:
        raise RangeError('Invalid ' + name)
    if isinstance(x, IntegerTypes):
        return x
    if not (x <= POS_SAFE_FLOAT and x >= 0.0):
        raise RangeError('Invalid ' + name)
    xi = LongType(x)
    if xi != x:
        raise RangeError('Invalid ' + name)
    return xi
# end qualifyIndex


# like qualifyIndexAllowInfinity but x should be grater or equal than zero
def qualifyNaturalIndexAllowInfinity(x, name):
    if isinstance(x, bool) or not isinstance(x, NumberTypes):
        raise TypeError("'" + type(x).__name__ + "' cannot be used as an " + name)
    if x < 0:
        raise RangeError('Invalid ' + name)
    if isinstance(x, IntegerTypes):
        return x
    if isInf(x):
        return x
    if not (x <= POS_SAFE_FLOAT and x >= NEG_SAFE_FLOAT):
        raise RangeError('Invalid ' + name)
    xi = LongType(x)
    if xi != x:
        raise RangeError('Invalid ' + name)
    return xi
# end qualifyIndex


# check if the parameter is an natural number and clamp it to the length
def clampNaturalIndexToLength(n, l, name):
    n = qualifyNaturalIndexAllowInfinity(n, name)
    if n > l:
        n = l
    # end if
    return n
# end clampNaturalIndexToLength


# check if the parameter is an integer and clamp it to the length or zero
def clampIndexToLength(n, l, name):
    n = qualifyIndexAllowInfinity(n, name)
    if n == 0:
        return n
    # end if
    if n < 0:
        n = l + n
        if n < 0:
            n = 0
        # end if
    elif n > l:
        n = l
    # end if
    return n
# end clampIndexToLength


# Container Operations


# @length
# return the length of this
# @length is null-safe, if the object is null, it will return 0
# however, if the object doesn't support __len__, a TypeError will be thrown
def length(self):
    if self is None:
        return 0
    return len(self)
# end length


# @isEmpty
# return true if this is an empty container (length is 0)
# @isEmpty is null-safe, if the object is null, it will return true
# however, if the object doesn't support __len__, a TypeError will be thrown
def isEmpty(self):
    if self is None:
        return True
    return not len(self)
# end isEmpty


# @push
# like es Array::push
# the target must be mutable
def push(self, *es):
    l0 = len(self)
    l1 = len(es)
    if isinstance(self, MutableSequence):
        if l1 == 1:
            self.append(es[0])
        elif l1 > 1:
            self.extend(es)
        # end if
    else:
        self[l0:] = es
    # end if
    return l0 + l1
# end push


# @pop
# like es Array::pop
# the target must be mutable
# throw if the target is empty
def pop(self):
    if isinstance(self, MutableSequence):
        return self.pop()
    l0 = len(self)
    if l0 == 0:
        raise IndexError('pop from empty sequence')
    e = self[l0 - 1]
    self[(l0 - 1):] = ()
    return e
# end push


# @shift
# like es Array::shift
# the target must be mutable
def shift(self):
    if isinstance(self, MutableSequence):
        return self.pop(0)
    l = len(self)
    if l == 0:
        raise IndexError('shift from empty sequence')
    v = self[0]
    del self[0]
    return v
# end shift


# @unshift
# like es Array::unshift
# the target must be mutable
def unshift(self, *es):
    l0 = len(self)
    l1 = len(es)
    if isinstance(self, MutableSequence):
        if l1 == 0:
            return l0
        elif l1 == 1:
            self.insert(0, es[0])
            return l0 + 1
        # end if
    # end if
    self[0:0] = es
    return l0 + l1
# end unshift


# @slice
# like es Array::slice
def slice(self, start = 0, end = Infinity):
    l = len(self)
    s = clampIndexToLength(start, l, 'start index')
    e = clampIndexToLength(end, l, 'end index')
    return self[s:e]
# end slice


# @splice
# like es Array::slice but returns nothing
def splice(self, start = Infinity, deleteCount = Infinity, *items):
    l = len(self)
    s = clampIndexToLength(start, l, 'start index')
    # throw error for negative deleteCount rather than fix it
    ld = clampNaturalIndexToLength(deleteCount, l - s, 'delete count')
    self[s:(s + ld)] = items
# end splice


# list.of
def list_of(*v):
    return list(v)
# end list_of


# tuple.of
def tuple_of(*v):
    return v
# end tuple_of
