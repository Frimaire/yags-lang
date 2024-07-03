# -*- coding: utf-8 -*-
# iterator helpers for python 3
from __future__ import print_function, absolute_import, division, generators
from collections.abc import Iterator
from itertools import takewhile, dropwhile
from .compat import RangeError, undefined, StringType

from .operator import coerceBoolean, coerceNot
from .container import qualifyNaturalIndexAllowInfinity
from .function import bindThis


class NotIterable(TypeError):
    def __init__(self, obj):
        super(NotIterable, self).__init__("'" + type(obj).__name__ + "' object is not iterable")
    # end __init__
# end NotIterable


# get the iterator's next
def _get_next(origin):
    it = iter(origin)
    return bindThis(next, it)
# end _get_next


# wrapped iterator
class IterWrapper(Iterator):
    __slots__ = ('_orig_next', 'finished')

    # next the origin iterator
    def step(self):
        if self.finished:
            raise StopIteration()
        abrupt = True
        try:
            item = self._orig_next()
            abrupt = False
            return item
        finally:
            # "IfAbruptCloseIterator"
            # if the supplied iterator throws error, self will be closed
            if abrupt:
                self.finished = True
            # end if
        # end try
    # end step

    # __next__(), can be overridden by sub-classes
    def __next__(self):
        return self.step()
    # end __next__

    # used for python 2 only
    def next(self):
        return self.__next__()
    # end next

    # constructor
    # @param {Iterable} origin, the origin object, should be iterable
    def __init__(self, origin):
        self.finished = False
        if isinstance(origin, IterWrapper):
            self._orig_next = origin.__next__
        else:
            self._orig_next = _get_next(origin)
    # end __init__
# end class IterWrapper


# get the iterator
def _iternx(origin):
    if isinstance(origin, IterWrapper):
        return origin.__next__
    return _get_next(origin)
# end _iternx


# helper class for array destructuring assignment
class DestrAssign(IterWrapper):
    __slots__ = ()

    # next item
    # if the iterator ends, a RangeError will be thrown
    # for optional parameter, use step() instead (throws StopIteration)
    def fetch(self):
        try:
            return self.step()
        except StopIteration:
            raise RangeError('no enough arguments to destructure')
    # end fetch

    # finalize the destructuring assignment for rest parameter
    # collect the rest element into a list
    def finalize(self, rest):
        return list(self)
    # end finalize
# end class DestrAssign


# Iterator Helpers
# see https://github.com/tc39/proposal-iterator-helpers


def _always(v):
    return True
# end _always


def _never(v):
    return False
# end _never


# iterator helper class for take/drop
class _LimitedIter(IterWrapper):
    __slots__ = ('limit', 'count')

    def __next__(self):
        o = self.step()
        self.count = self.count + 1
        return o
    # end next

    def gate(self, *v):
        return self.count <= self.limit
    # end next

    def __init__(self, orig, lim):
        super(_LimitedIter, self).__init__(orig)
        self.limit = lim
        self.count = 0
    # end __init__
# end _LimitedIter


# @take method
def take(self, limit):
    l = qualifyNaturalIndexAllowInfinity(limit, 'limit')
    it = _LimitedIter(self, l)
    return takewhile(it.gate, it)
# end take


# @drop method
def drop(self, limit):
    l = qualifyNaturalIndexAllowInfinity(limit, 'limit')
    it = _LimitedIter(self, l)
    return dropwhile(it.gate, it)
# end drop


# @forEach
# cb(item, index)
# the last parameter (object itself) no longer exists in the iterator version
def forEach(self, cb):
    if not callable(cb):
        raise TypeError('parameter callback of forEach is not a function')
    k = 0
    nx = _iternx(self)
    try:
        while True:
            v = nx()
            cb(v, k)
            k = k + 1
        # end while
    except StopIteration:
        pass
    # end try
# end forEach


# iterator helper class for map
class _MappedIter(IterWrapper):
    __slots__ = ('count', 'map')

    def __next__(self):
        # IfAbruptCloseIterator
        abrupt = True
        try:
            o = self.step()
            k = self.count
            r = self.map(o, k)
            self.count = k + 1
            abrupt = False
            return r
        finally:
            if abrupt:
                self.finished = True
            # end if
        # end try
    # end next

    def __init__(self, orig, map):
        super(_MappedIter, self).__init__(orig)
        self.count = 0
        self.map = map
    # end __init__
# end _MappedIter


# @map method
def imap(self, cb):
    if not callable(cb):
        raise TypeError('parameter callback of map is not a function')
    mc = _MappedIter(self, cb)
    # qualify the iterator by drop(0)
    return dropwhile(_never, mc)
# end map


# iterator helper class for map
class _FilteredIter(IterWrapper):
    __slots__ = ('origcb', 'count')

    def filter(self, val):
        # IfAbruptCloseIterator
        abrupt = True
        try:
            k = self.count
            r = coerceBoolean(self.origcb(val, k))
            self.count = k + 1
            abrupt = False
            return r
        finally:
            if abrupt:
                self.finished = True
            # end if
        # end try
    # end next

    def __init__(self, orig, cb):
        super(_FilteredIter, self).__init__(orig)
        self.origcb = cb
        self.count = 0
    # end __init__
# end _FilteredIter


# @filter
def ifilter(self, cb):
    if not callable(cb):
        raise TypeError('parameter callback of filter is not a function')
    mc = _FilteredIter(self, cb)
    return filter(mc.filter, mc)
# end filter


# helper class for flatMap
# chain is not lazy, cannot be used
class _FlattenIter(IterWrapper):
    __slots__ = ('_iinext', '_iiavail')

    def __next__(self):
        if self.finished:
            raise StopIteration()
        # end if
        while True:
            if self._iiavail:
                iir = self._iinext
                abrupt = True
                try:
                    item = iir()
                    abrupt = False
                    return item
                except StopIteration:
                    self._iiavail = False
                    abrupt = False
                finally:
                    if abrupt:
                        # IfAbruptCloseIterator
                        self.finished = True
                # end try
            # end if
            iir = self.step()
            self._iiavail = True
            abrupt = True
            try:
                self._iinext = _iternx(iir)
                abrupt = False
            finally:
                if abrupt:
                    self.finished = True
                # end if
            # end try
        # end while
    # end next

    def __init__(self, origin):
        super(_FlattenIter, self).__init__(origin)
        self._iinext = None
        self._iiavail = False
    # end __init__
# end _FlattenIter


# @flatMap
def flatMap(self, cb):
    if not callable(cb):
        raise TypeError('parameter callback of flatMap is not a function')
    # use a deop(0) to qualify the iterator
    return dropwhile(_never, _FlattenIter(_MappedIter(self, cb)))
# end flatMap


# @some
def some(self, cb):
    if not callable(cb):
        raise TypeError('parameter callback of some is not a function')
    k = 0
    nx = _iternx(self)
    try:
        while True:
            v = nx()
            if coerceBoolean(cb(v, k)):
                return True
            # end if
            k = k + 1
        # end while
    except StopIteration:
        pass
    # end try
    return False
# end some


# @every
def every(self, cb):
    if not callable(cb):
        raise TypeError('parameter callback of every is not a function')
    k = 0
    nx = _iternx(self)
    try:
        while True:
            v = nx()
            if coerceNot(cb(v, k)):
                return False
            # end if
            k = k + 1
        # end while
    except StopIteration:
        pass
    # end try
    return True
# end every


# @find
def find(self, cb):
    if not callable(cb):
        raise TypeError('parameter callback of find is not a function')
    k = 0
    nx = _iternx(self)
    try:
        while True:
            v = nx()
            if coerceBoolean(cb(v, k)):
                return v
            # end if
            k = k + 1
        # end while
    except StopIteration:
        pass
    # end try
    return None
# end find


# @findIndex
def findIndex(self, cb):
    if not callable(cb):
        raise TypeError('parameter callback of find is not a function')
    k = 0
    nx = _iternx(self)
    try:
        while True:
            v = nx()
            if coerceBoolean(cb(v, k)):
                return k
            # end if
            k = k + 1
        # end while
    except StopIteration:
        pass
    # end try
    return -1
# end find


# @reduce
def reduce(self, cb, initval = undefined):
    if not callable(cb):
        raise TypeError('parameter callback of reduce is not a function')
    k = 0
    nx = _iternx(self)
    if initval is undefined:
        try:
            initval = nx()
            k = 1
        except StopIteration:
            pass
        # end try
    # end if
    if initval is undefined:
        raise TypeError('Reduce of empty iterable with no initial value')
    acc = initval
    try:
        while True:
            v = nx()
            acc = cb(acc, v, k)
            k = k + 1
        # end while
    except StopIteration:
        pass
    # end try
    return acc
# end reduce


def _toStr(v, k):
    return StringType(v)
# end _toStr


# @join
# like es Array::join but iterator version
def join(self, s = u','):
    return s.join(_MappedIter(self, _toStr))
# end join
