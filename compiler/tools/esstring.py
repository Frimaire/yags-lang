# Copyright 2024 Frimaire
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import print_function, absolute_import, division, generators


def __():
    from sys import version_info
    global String, ES_LINE_TERMINATOR, ES_WHITE_SPACE

    ES_LINE_TERMINATOR = (u'\x0A', u'\x0D', u'\u2028', u'\u2029')
    ES_WHITE_SPACE = (u'\x09', u'\x0B', u'\x0C', u'\x20', u'\xA0',
                      u'\u1680', u'\u180E', u'\u2000', u'\u2001', u'\u2002',
                      u'\u2003', u'\u2004', u'\u2005', u'\u2006', u'\u2007',
                      u'\u2008', u'\u2009', u'\u200A', u'\u202F', u'\u205F',
                      u'\u3000', u'\uFEFF')

    ISPY2 = version_info.major < 3
    strT = type(u'')
    byteT = type(b'')
    if ISPY2:
        intT = (int, long)
        uchr = unichr
        try:
            uchr(65536)
        except:
            raise Exception('wide Python 2 build is required by String library')
        from itertools import imap
    else:
        intT = int
        uchr = chr
        imap = map

    def isstr(o):
        return isinstance(o, (strT, byteT))

    def tostr(o):
        if isinstance(o, strT):
            # "standardize" it
            return strT(o)
        if isinstance(o, byteT):
            return byteT(o)
        raise TypeError('A string is required.')

    def toindex(o, defval, name):
        if o is None:
            return defval
        if isinstance(o, intT):
            return o
        T = type(o)
        if hasattr(T, '__index__') and callable(T.__index__):
            o = T.__index__(o)
            if isinstance(o, intT):
                return o
        raise TypeError('Parameter ' + name + ' must be integers')

    WHITE_SPACE_LINE_TERMINATOR_A = b''.join((
        b'\x09', b'\x0B', b'\x0C', b'\x20', b'\xA0',
        b'\x0A', b'\x0D'
    ))
    WHITE_SPACE_LINE_TERMINATOR_W = u''.join((
        u'\x09', u'\x0B', u'\x0C', u'\x20', u'\xA0',
        u'\u1680', u'\u180E', u'\u2000', u'\u2001', u'\u2002',
        u'\u2003', u'\u2004', u'\u2005', u'\u2006', u'\u2007',
        u'\u2008', u'\u2009', u'\u200A', u'\u202F', u'\u205F',
        u'\u3000', u'\uFEFF',
        u'\x0A', u'\x0D', u'\u2028', u'\u2029'
    ))

    class StringClass(type):
        __slots__ = ()

        # String()
        def __call__(T, value = u''):
            # For unicode String, return as-is.
            if isinstance(value, strT):
                return strT(value)
            # special literals
            if value is None:
                return "null"
            if value is True:
                return "true"
            if value is False:
                return "false"
            # For bytes, convert to binary String "literally", that is,
            #   treat the byte as its corresponding unicode code (in Latin-1).
            # \x00 => \u0000, \x01 => \u0001, ..., \xff => \u00ff
            if isinstance(value, byteT):
                return byteT.decode(value, "Latin-1")
            if isinstance(value, bytearray):
                return bytearray.decode(value, "Latin-1")
            # Otherwise, follow the behavior of their classes
            return strT(value)

        # only unicode string instanceof String
        def __instancecheck__(T, this):
            return isinstance(this, strT)

        def __subclasscheck__(T, R):
            return issubclass(R, strT)

        # String.fromCharCode but the "char code" in python is actually a code point
        def fromCharCode(T, *chars):
            return ''.join(imap(uchr, chars))

        # String.prototype.charCodeAt
        # ES5 15.5.4.5
        # charCodeAt will throw an IndexError if there is no character at that
        # position instead of returning NaN.
        def charCodeAt(T, this, index = None):
            this = tostr(this)
            index = toindex(index, 0, 'position of charCodeAt')
            return ord(this[index])

        # String.prototype.concat
        # 15.5.4.6
        # All parameters including the first parameter will be converted to String.
        def concat(T, *strs):
            return ''.join(imap(String, strs))

        # String.prototype.indexOf
        # 15.5.4.7
        def indexOf(T, this, searchStr, position = None):
            this = tostr(this)
            searchStr = tostr(searchStr)
            position = min(max(toindex(position, 0, 'start position of indexOf'), 0), len(this))
            if isinstance(this, strT) and isinstance(searchStr, strT):
                return strT.find(this, searchStr, position)
            if isinstance(this, byteT) and isinstance(searchStr, byteT):
                return byteT.find(this, searchStr, position)
            # convert to unicode
            this = String(this)
            searchStr = String(searchStr)
            return strT.find(this, searchStr, position)

        # String.prototype.lastIndexOf
        # 15.5.4.8
        def lastIndexOf(T, this, searchStr, pos = None):
            this = tostr(this)
            searchStr = tostr(searchStr)
            pos = min(max(toindex(pos, len(this), 'start position of lastIndexOf'), 0), len(this))
            if pos < 0:
                pos = 0
            # the largest possible nonnegative integer k not larger than start
            # py's rfind requires "end position"
            pos = pos + len(searchStr)
            if isinstance(this, strT) and isinstance(searchStr, strT):
                return strT.rfind(this, searchStr, 0, pos)
            if isinstance(this, byteT) and isinstance(searchStr, byteT):
                return byteT.rfind(this, searchStr, 0, pos)
            this = String(this)
            searchStr = String(searchStr)
            return strT.rfind(this, searchStr, 0, pos)

        # String.prototype.slice
        # 15.5.4.13
        def slice(T, this, start = None, end = None):
            this = tostr(this)
            start = toindex(start, 0, 'start position of slice')
            end = toindex(end, len(this), 'end position of slice')
            return this[start:end]

        # String.prototype.split
        # 15.5.4.14
        # currently regex is not supported
        # the member of the returned array is the same as the parameter "s"
        def split(T, this, separator = None, limit = None):
            this = tostr(this)
            # es requires <= 2 ** 32 - 1, useless here
            limit = toindex(limit, len(this), 'limit of split')
            if separator is None:
                if limit:
                    return [this]
                return []
            separator = tostr(separator)
            if not limit:
                return []
            # Here any negative limit will be treat as Infinity
            # since in Python there are no "ToUint32" operation
            if limit < 0:
                limit = len(this)
            if not len(separator):
                if len(this) == 0:
                    return []
                return list(this)[0:limit]
            if isinstance(this, strT):
                if isinstance(separator, byteT):
                    separator = String(separator)
                # in py, the list will have at most maxsplit+1 elements
                return strT.split(this, separator, limit)[0:limit]
            # this instanceof bytes
            if isinstance(separator, strT):
                try:
                    separator = strT.encode(separator, 'Latin-1')
                except:
                    # out of range, obviously nowhere to split in a bytes
                    return [this]
            return byteT.split(this, separator, limit)[0:limit]

        # String.prototype.substring
        # 15.5.4.15
        def substring(T, this, start = None, end = None):
            this = tostr(this)
            l = len(this)
            start = toindex(start, 0, 'start position of substring')
            end = toindex(end, l, 'end position of substring')
            finalStart = min(max(start, 0), l)
            finalEnd = min(max(end, 0), l)
            # substring sort the parameters
            return this[min(finalStart, finalEnd):max(finalStart, finalEnd)]

        # String.prototype.substr
        # B.2.3.1
        def substr(T, this, start = None, length = None):
            this = tostr(this)
            l = len(this)
            finalStart = toindex(start, 0, 'start position of substr')
            if finalStart < 0:
                finalStart = max(finalStart + l, 0)
            finalEnd = max(toindex(length, l, 'length of substr'), 0) + finalStart
            return this[finalStart:finalEnd]

        # String.prototype.toLowerCase
        # 15.5.4.16
        # There are actually differents.
        # For example, "\u2c2f".toLowerCase() is "\u2c5f"
        # but the same in python's tolower
        # We will not "polyfill" it since these characters are rarely used.
        def toLowerCase(T, this):
            this = tostr(this)
            return this.lower()

        # String.prototype.toUpperCase
        # 15.5.4.18
        def toUpperCase(T, this):
            this = tostr(this)
            return this.upper()

        # String.prototype.trim
        # 15.5.4.20
        def trim(T, this):
            this = tostr(this)
            if isinstance(this, strT):
                return strT.strip(this, WHITE_SPACE_LINE_TERMINATOR_W)
            return byteT.strip(this, WHITE_SPACE_LINE_TERMINATOR_A)

    def fakeInit(this, *_):
        raise TypeError('Illegal constructor.')

    String = StringClass('String', (object,), {
        '__init__': fakeInit
    })


__()
