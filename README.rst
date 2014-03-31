
.. image:: https://travis-ci.org/canni/switch.svg?branch=master
    :target: https://travis-ci.org/canni/switch

.. image:: https://coveralls.io/repos/canni/switch/badge.png?branch=master
    :target: https://coveralls.io/r/canni/switch?branch=master

.. image:: https://pypip.in/download/switch/badge.png
    :target: https://pypi.python.org/pypi/switch/
    :alt: Downloads


Switch
======

Changelog
---------

- v1.0.2: 100% unit test coverage


Simple example:
---------------

.. code-block:: python

    from switch import Switch

    def simple_example(val):
        with Switch(val) as case:
            if case(1):
                return 'Found 1'

            if case(2):
                return 'Found 2'

    assert simple_example(1) == 'Found 1'
    assert simple_example(2) == 'Found 2'
    assert simple_example('anything else') == None


Simple example with default case:
---------------------------------

.. code-block:: python

    from switch import Switch

    def simple_example_with_default(val):
        with Switch(val) as case:
            if case(1):
                return 'Found 1'

            if case(2):
                return 'Found 2'

            if case.default:
                return 'No love for 1 or 2?'

    assert simple_example_with_default(1) == 'Found 1'
    assert simple_example_with_default(2) == 'Found 2'
    assert simple_example_with_default('anything else') == 'No love for 1 or 2?'


Fall through example:
---------------------

.. code-block:: python

    from switch import Switch

    def fall_through_example(val):
        values = []

        with Switch(val) as case:
            if case(1, fall_through=True):
                values.append('Found 1')

            if case(2):
                values.append('Found 2')

            if case.default:
                values.append('No love for 1 or 2?')

        return values

    assert fall_through_example(1) == ['Found 1', 'Found 2']
    assert fall_through_example(2) == ['Found 2']
    assert fall_through_example('anything else') == ['No love for 1 or 2?']


Ouh! Callable too!:
-------------------

.. code-block:: python

    from switch import Switch

    def ouh_callable_too(val):
        values = []

        with Switch(val) as case:
            if case(1):
                values.append('Found 1')

            if case.call(lambda v: v < 100):
                values.append('Found <100')

            if case.default:
                values.append('No love for anything lower than 100?')

        return values

    assert ouh_callable_too(1) == ['Found 1']
    assert ouh_callable_too(50) == ['Found <100']
    assert ouh_callable_too('anything else') == ['No love for anything lower than 100?']


Fall through by default? NP!:
-----------------------------

.. code-block:: python

    from switch import CSwitch, Switch

    def fall_through_by_default(val):
        values = []

        with Switch(val, fall_through=True) as case:
            if case(1):
                values.append('Found 1')

            if case(2):
                values.append('Found 2')

            if case(3, fall_through=False):
                values.append('Found 3')

            if case(4):
                values.append('Found 4')

            if case.default:
                values.append('No love for 1, 2, 3 or 4?')

        return values


    def cswitch_shortcut(val):
        values = []

        with CSwitch(val) as case:
            if case(1):
                values.append('Found 1')

            if case(2):
                values.append('Found 2')

            if case(3, fall_through=False):
                values.append('Found 3')

            if case(4):
                values.append('Found 4')

            if case.default:
                values.append('No love for 1, 2, 3 or 4?')

        return values

    assert fall_through_by_default(1) == ['Found 1', 'Found 2', 'Found 3']
    assert fall_through_by_default(2) == ['Found 2', 'Found 3']
    assert fall_through_by_default(3) == ['Found 3']
    assert fall_through_by_default(4) == ['Found 4']
    assert fall_through_by_default('anything else') == ['No love for 1, 2, 3 or 4?']

    assert cswitch_shortcut(1) == fall_through_by_default(1)
    assert cswitch_shortcut(2) == fall_through_by_default(2)
    assert cswitch_shortcut(3) == fall_through_by_default(3)
    assert cswitch_shortcut(4) == fall_through_by_default(4)
    assert cswitch_shortcut('anything else') == fall_through_by_default('anything else')


Having a case after a default is a bad thing*:
----------------------------------------------

* *Unless some case executes early and finishes without fall through.

.. code-block:: python

    from switch import Switch

    def case_after_default_is_baad(val):
        values = []

        with Switch(val) as case:
            if case(1):
                values.append('Found 1')

            if case.default:
                values.append('Found default')

            if case('this is baad'):
                values.append('Should not happen!')

        return values

    assert case_after_default_is_baad(1) == ['Found 1']

    try:
        case_after_default_is_baad('this is baad')
        assert False
    except SyntaxError:
        assert True
