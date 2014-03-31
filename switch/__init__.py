# -*- coding: utf-8 -*-

from __future__ import with_statement

__version__ = '1.0.2'
__all__ = ['CSwitch', 'Switch']


class Switch(object):
    """
    Switch, simple implementation of switch statement for Python, eg:

    >>> def test_switch(val):
    ...   ret = []
    ...   with Switch(val) as case:
    ...     if case(1, fall_through=True):
    ...       ret.append(1)
    ...     if case(2):
    ...       ret.append(2)
    ...     if case.call(lambda v: 2 < v < 4):
    ...       ret.append(3)
    ...     if case.call(lambda v: 3 < v < 5, fall_through=True):
    ...       ret.append(4)
    ...     if case(5):
    ...       ret.append(5)
    ...     if case.default:
    ...       ret.append(6)
    ...   return ret
    ...
    >>> test_switch(1)
    [1, 2]

    >>> test_switch(2)
    [2]

    >>> test_switch(3)
    [3]

    >>> test_switch(4)
    [4, 5]

    >>> test_switch(5)
    [5]

    >>> test_switch(7)
    [6]


    >>> def test_switch_default_fall_through(val):
    ...   ret = []
    ...   with Switch(val, fall_through=True) as case:
    ...     if case(1):
    ...       ret.append(1)
    ...     if case(2):
    ...       ret.append(2)
    ...     if case.call(lambda v: 2 < v < 4):
    ...       ret.append(3)
    ...     if case.call(lambda v: 3 < v < 5, fall_through=False):
    ...       ret.append(4)
    ...     if case(5):
    ...       ret.append(5)
    ...     if case.default:
    ...       ret.append(6)
    ...   return ret
    ...
    >>> test_switch_default_fall_through(1)
    [1, 2, 3, 4]

    >>> test_switch_default_fall_through(2)
    [2, 3, 4]

    >>> test_switch_default_fall_through(3)
    [3, 4]

    >>> test_switch_default_fall_through(4)
    [4]

    >>> test_switch_default_fall_through(5)
    [5]

    >>> test_switch_default_fall_through(7)
    [6]
    """

    class StopExecution(Exception):
        pass

    def __init__(self, test_value, fall_through=False):
        self._value = test_value
        self._fall_through = None
        self._default_fall_through = fall_through
        self._use_default = True
        self._default_used = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is self.StopExecution:
            return True

        return False

    def __call__(self, expr, fall_through=None):
        return self.call(lambda v: v == expr, fall_through)

    def call(self, call, fall_through=None):
        if self._default_used:
            raise SyntaxError('Case after default is prohibited')

        if self._finished:
            raise self.StopExecution()
        elif call(self._value) or self._fall_through:
            self._use_default = False
            if fall_through is None:
                self._fall_through = self._default_fall_through
            else:
                self._fall_through = fall_through
            return True

        return False

    @property
    def default(self):
        if self._finished:
            raise self.StopExecution()

        self._default_used = True

        if self._use_default:
            return True

        return False

    @property
    def _finished(self):
        return self._use_default is False and self._fall_through is False


class CSwitch(Switch):
    """
    CSwitch is a shortcut to call Switch(test_value, fall_through=True)
    """
    def __init__(self, test_value):
        super(CSwitch, self).__init__(test_value, fall_through=True)
