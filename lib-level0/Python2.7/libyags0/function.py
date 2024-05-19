# -*- coding: utf-8 -*-
# function helpers for python 2
from __future__ import print_function, absolute_import, division, generators
from functools import partial
from importlib import import_module


# variable slot for closured variables
class VarSlot(object):
    __slots__ = ('val',)

    def __getattr__(self, name):
        # __getattr__ will be called only if val is undefined, so throw directly
        # if the attribute is found through the normal mechanism, __getattr__() is not called
        if name == 'val':
            raise UnboundLocalError('local variable referenced before assignment')
        return super(VarSlot, self).__getattribute__(name)
    # end __getattr__
# end VarSlot


# import
def makeImport(name):
    kd = name.rfind('.')
    if kd < 0:
        pkg = False
        pn = None
    else:
        pkg = True
        pn = name[0:kd]
    # end if

    def impfn(mod):
        if mod[0:1] == '.' and not pkg:
            raise ValueError('Attempted relative import in non-package ' + name)
        return import_module(mod, pn)
    # end impfn
    return impfn
# end makeImport


# @bind
# like Function::bind but this pointer can no longer be overridden
def bind(self, *argv, **argo):
    if not callable(self):
        raise TypeError('Bind must be called on a function')
    return partial(self, *argv, **argo)
# end bind


# @apply
# like Function::apply but
#   1. this pointer can no longer be overridden
#   2. a dict containing the keyword arguments can be used as the second argument
def apply(self, argv = [], argo = {}):
    return self(*argv, **argo)
# end apply


# for python2, instancemethod
# for python3, method
# bindThis(function, this)
bindThis = type(VarSlot().__getattr__)
