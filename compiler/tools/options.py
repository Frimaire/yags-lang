# -*- coding: utf-8 -*-

# the options (experimental functions)

__all__ = ('options',)


class _Opts(object):
    __slots__ = (
        'enableImplicitBooleanConversion',
        'enableTupleSubscription'
    )

    def __init__(this):
        this.enableImplicitBooleanConversion = False
        this.enableTupleSubscription = False
    # end __init__
# end class Config


options = _Opts()
