# -*- coding: utf-8 -*-
# compatibility utils of YAGS runtime for python 2
from __future__ import print_function, absolute_import, division, generators
from sys import version_info


if version_info.major != 2 or version_info.minor != 7:
    raise TypeError('only Python 2.7 is supported')
# end if
ISPY2 = True


# RangeError is an alias of ValueError
RangeError = ValueError


# Integer
LongType = long
IntegerTypes = (long, int)


def isIntegerType(x):
    return isinstance(x, IntegerTypes)
# end isIntegerType


# Number
# float type between 32-bit to 256-bit is required
FloatType = float
NumberTypes = IntegerTypes + (float,)


# check if n is safe integer
def isSafeInt(n):
    return LongType(float(n + 1)) == n + 1 and \
        LongType(float(n)) == n and \
        LongType(float(n - 1)) == n - 1
# end isSafeFloat


def _testSafe():
    n = 1
    while True:
        m = n << 1
        if isSafeInt(m):
            n = m
        else:
            break
        # end if
    # end while
    k = n >> 1
    while k != 0:
        m = n | k
        if isSafeInt(m):
            n = m
        # end if
        k = k >> 1
    # end while
    # normally 2 ^ 53 - 1
    safep = n
    n = 1
    while True:
        m = n << 1
        if isSafeInt(-m):
            n = m
        else:
            break
        # end if
    # end while
    k = n >> 1
    while k != 0:
        m = n | k
        if isSafeInt(-m):
            n = m
        # end if
        k = k >> 1
    # end while
    safen = -n
    return (LongType(safep), LongType(safen))
# end _testSafe


# check the precision
(POS_SAFE_INTEGER, NEG_SAFE_INTEGER) = _testSafe()
# end if
POS_SAFE_FLOAT = float(POS_SAFE_INTEGER)
NEG_SAFE_FLOAT = float(NEG_SAFE_INTEGER)
if POS_SAFE_INTEGER < 16777215 or NEG_SAFE_INTEGER > -16777215:
    raise TypeError('float with at least single preision (32-bit) is required')
elif POS_SAFE_INTEGER > 2 ** 237 - 1 or NEG_SAFE_INTEGER < -(2 ** 237 - 1):
    raise TypeError('cannot detect the precision of float type')
# end if


# Not a Number
def isNaN(x):
    return x != x
# end isNaN


# Infinity
def isInf(x):
    return isNaN(x - x) and not isNaN(x)
# end isNaN


_maxf32 = float(2 ** 128 - 1)
if isNaN(_maxf32 - _maxf32):
    raise TypeError('float with at least single preision (32-bit) is required')
# end if
Infinity = 1e78914
NaN = Infinity - Infinity
if not isNaN(NaN):
    raise TypeError('cannot find the infinite value')
# end if


# String
uchr = unichr
uord = ord
StringType = unicode
BytesType = str


# iterator varsion range
range = xrange


# The undefined flag, only used internally
undefined = object()
