# -*- coding: utf-8 -*-

from __future__ import with_statement

import pytest

from switch import Switch


def switch(val):
   ret = []
   with Switch(val) as case:
       if case(1, fall_through=True):
           ret.append(1)
       if case(2):
           ret.append(2)
       if case.call(lambda v: 2 < v < 4):
           ret.append(3)
       if case.call(lambda v: 3 < v < 5, fall_through=True):
           ret.append(4)
       if case(5):
           ret.append(5)
       if case.default:
           ret.append(6)
   return ret


def switch_default_fall_through(val):
   ret = []
   with Switch(val, fall_through=True) as case:
       if case(1):
           ret.append(1)
       if case(2):
           ret.append(2)
       if case.call(lambda v: 2 < v < 4):
           ret.append(3)
       if case.call(lambda v: 3 < v < 5, fall_through=False):
           ret.append(4)
       if case(5):
           ret.append(5)
       if case.default:
           ret.append(6)
   return ret


@pytest.mark.parametrize(('value', 'expected'), (
    (1, [1, 2]),
    (2, [2]),
    (3, [3]),
    (4, [4, 5]),
    (5, [5]),
    (10, [6]),
))
def test_switch(value, expected):
    assert switch(value) == expected


@pytest.mark.parametrize(('value', 'expected'), (
    (1, [1, 2, 3, 4]),
    (2, [2, 3, 4]),
    (3, [3, 4]),
    (4, [4]),
    (5, [5]),
    (10, [6]),
))
def test_switch_fall_through(value, expected):
    assert switch_default_fall_through(value) == expected


def test_return_early_without_syntax_error():
    with Switch(1) as case:
        if case(1):
            assert True
        if case(2):
            assert False
        if case.default:
            assert False
        if case(3):
            assert False

    assert True


def test_return_early_on_default():
    with Switch(1) as case:
        if case(1):
            assert True
        if case.default:
            assert False
        if case(2):
            assert False

    assert True


def test_no_side_effects():
    class TestObj(object):
        def __init__(self, val):
            self.val = val

        def __eq__(self, other):
            if other.val == self.val:
                return True

            assert False

    with Switch(TestObj(1)) as case:
        if case(TestObj(1)):
            assert True
        if case(TestObj(2)):
            assert False

    with Switch(TestObj(1)) as case:
        if case(TestObj(1)):
            assert True
        if case.default:
            assert False


def test_exception():
    with pytest.raises(SyntaxError):
        with Switch(2) as case:
            if case(1):
                assert False
            if case.default:
                assert True
            if case(2):
                assert False
