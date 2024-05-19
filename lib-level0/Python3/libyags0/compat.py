# -*- coding: utf-8 -*-
# compatibility utils of YAGS runtime for python 3
from __future__ import print_function, absolute_import, division, generators
from math import inf, isinf, isnan
from sys import version_info


if version_info.major != 3 or version_info.minor < 4:
    raise TypeError('Python 3.4+ is required')
# end if
ISPY2 = False


# RangeError is an alias of ValueError
RangeError = ValueError


# Integer
LongType = int
IntegerTypes = (int,)


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
isNaN = isnan
isInf = isinf


_maxf32 = float(2 ** 128 - 1)
if isNaN(_maxf32 - _maxf32):
    raise TypeError('float with at least single preision (32-bit) is required')
# end if
Infinity = inf
NaN = Infinity - Infinity
if not isNaN(NaN):
    raise TypeError('cannot find the infinite value')
# end if


# String
uchr = chr
uord = ord
StringType = str
BytesType = bytes


# iterator varsion range
range = range


# The undefined flag, only used internally
undefined = object()
