# -*- coding: utf-8 -*-
# YAGS Level 0 run-time library for Python2
# DO NOT use this library in your code directly unless you are developing this library.

# Copyright 2024 Frimaire and other contributors
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
#

from __future__ import print_function, absolute_import, division, generators

__all__ = (
    # base types
    '__x_tup', '__x_errT',
    # operators
    '__x_eq', '__x_ne', '__x_typ', '__x_cb', '__x_not', '__x_iof', '__x_inc', '__x_dec',
    # implicit boolean conversion
    '__x_tob', '__x_tnb',
    # miscellaneous
    '__x_var', '__x_imf', '__x_lst', '__x_tupof',
    # magic functions
    '__x_at_take', '__x_at_drop', '__x_at_forEach', '__x_at_map', '__x_at_filter',
    '__x_at_flatMap', '__x_at_some', '__x_at_every', '__x_at_find', '__x_at_findIndex',
    '__x_at_reduce', '__x_at_join', '__x_at_bind', '__x_at_apply', '__x_at_length',
    '__x_at_isEmpty', '__x_at_push', '__x_at_pop', '__x_at_shift', '__x_at_unshift',
    '__x_at_slice', '__x_at_splice',
    '__x_at_has'
    # class
    '__x_dcls', '__x_dpif', '__x_dpsf', '__x_prmT', '__x_csgT', '__x_cpgT', '__x_objT',
    '__x_smet', '__x_prop',
    # Infinity and NaN
    'Infinity', 'NaN'
)

# base types
__x_tup = tuple
__x_errT = Exception

# operators
from .operator import strictEqual as __x_eq
from .operator import strictInequal as __x_ne
from .operator import typeof as __x_typ
from .operator import coerceBoolean as __x_cb
from .operator import coerceNot as __x_not
from .operator import instanceof as __x_iof
from .operator import inc as __x_inc
from .operator import dec as __x_dec

# miscellaneous
from .function import makeImport as __x_imf
from .function import VarSlot as __x_var
from .container import list_of as __x_lst
from .container import tuple_of as __x_tupof

# magic functions
from .container import length as __x_at_length
from .container import isEmpty as __x_at_isEmpty
from .container import push as __x_at_push
from .container import pop as __x_at_pop
from .container import shift as __x_at_shift
from .container import unshift as __x_at_unshift
from .container import slice as __x_at_slice
from .container import splice as __x_at_splice
from .function import bind as __x_at_bind
from .function import apply as __x_at_apply
from .iterhelper import take as __x_at_take
from .iterhelper import drop as __x_at_drop
from .iterhelper import forEach as __x_at_forEach
from .iterhelper import imap as __x_at_map
from .iterhelper import ifilter as __x_at_filter
from .iterhelper import flatMap as __x_at_flatMap
from .iterhelper import some as __x_at_some
from .iterhelper import every as __x_at_every
from .iterhelper import find as __x_at_find
from .iterhelper import findIndex as __x_at_findIndex
from .iterhelper import reduce as __x_at_reduce
from .iterhelper import join as __x_at_join
from .iterhelper import has as __x_at_has

# class tools
from .classtool import defineClass as __x_dcls
from .classtool import definePrivateInstanceField as __x_dpif
from .classtool import definePrivateStaticField as __x_dpsf
from .classtool import PrivateMap as __x_prmT
from .classtool import StaticPrivateGate as __x_csgT
from .classtool import ClassPrivateGate as __x_cpgT
__x_objT = object
__x_smet = staticmethod
__x_prop = property

# Infinity and NaN
from .compat import Infinity
from .compat import NaN

# (experimentally) implicit boolean conversion
from .operator import toBoolean as __x_tob
from .operator import toNotBoolean as __x_tnb
