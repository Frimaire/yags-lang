from __future__ import print_function, absolute_import, division, generators

__all__ = ('ArrayList', 'StrTool', 'printf')


# linear container ArrayList
class ArrayList(object):
    __slots__ = ('_r',)

    # initializer
    # similar to Array.from
    def __init__(self, src = None):
        if src is None:
            self._r = []
        elif isinstance(src, ArrayList):
            self._r = src._r[:]
        elif isinstance(src, list):
            self._r = src[:]
        else:
            self._r = list(src)
    # end __init__

    # length getter
    @property
    def length(self):
        return len(self._r)
    # end get length

    # get the item
    # @param {Number} index can be negative
    # throw RangeError if index out of range
    def get(self, index):
        i = checkIndexRange(index, self.length)
        return self._r[i]
    # end get

    # set the item
    # @param {Number} index can be negative
    # throw RangeError if index out of range
    def set(self, index, v):
        l = self.length
        i = checkIndexRange(index, l)
        self._r[i] = v
        return self
    # end set

    # Array::push but only one item is allowed
    def push(self, v):
        self._r.append(v)
    # end push

    # Array::unshift but only one item is allowed
    def unshift(self, v):
        return self._r.insert(0, v)
    # end push

    # Array::reverse
    def reverse(self):
        self._r.reverse()
        return self
    # end reverse

    # iterate the list
    # @param {Function} callback(item, index, self)
    # callback can return boolean false to stop the iteration
    def forEach(self, callback):
        k = 0
        a = self._r
        l = self.length
        while k < l:
            if callback(a[k], k, self) is False:
                break
            k = k + 1
        # end while
    # end forEach

    # Array::join
    def join(self, s = u','):
        return s.join(map(str, self._r))
    # end join
# end class ArrayList


def checkIndex(index):
    i = int(index)
    if i != index:
        raise TypeError(u'index is not an integer')
    return i
# end checkIndex


def checkIndexRange(i, l):
    i = checkIndex(i)
    if i >= 0:
        if i >= l:
            raise IndexError(u'index (%d) out of range (%d)' % (i, l))
        return i
    if i < -l:
        raise IndexError(u'index (%d) out of range (%d)' % (i, l))
    return i + l
# end checkIndexRange


class StrTool(object):
    @staticmethod
    def codePointAt(s, k = 0):
        return ord(s[k])
    # end codePointAt

    @staticmethod
    def strlen(s):
        return len(s)
    # end strlen

    @staticmethod
    def toCodePointString(n):
        if n <= 0xffff:
            return u'\\u%04X' % n
        return u'\\U%08X' % n
    # end toCodePointString

    @staticmethod
    def str(n):
        return type(u'')(n)
    # end str

    @staticmethod
    def typeName(o):
        return str(type(o).__name__)
    # end typeName

    def __init__(self):
        raise TypeError(u'Illegal constructor')
    # end __init__
# end class StrTool


# vsprintf
def printf(s, v):
    if not isinstance(v, (list, tuple)):
        raise TypeError('argv is required')
    return s % tuple(v)
# end vsprintf

