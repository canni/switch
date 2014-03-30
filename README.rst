.. image:: https://travis-ci.org/canni/switch.svg?branch=master
   :target: https://travis-ci.org/canni/switch


Switch
======

Default behaviour
-----------------

.. code-block:: python

   def test_switch(val):
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

   assert test_switch(1) == [1, 2]
   assert test_switch(2) == [2]
   assert test_switch(3) == [3]
   assert test_switch(4) == [4, 5]
   assert test_switch(5) == [5]
   assert test_switch(7) == [6]


Default fallthrough
-------------------

.. code-block:: python

   from switch import Switch

   def test_switch(val):
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

   assert test_switch(1) == [1, 2, 3, 4]
   assert test_switch(2) == [2, 3, 4]
   assert test_switch(3) == [3, 4]
   assert test_switch(4) == [4]
   assert test_switch(5) == [5]
   assert test_switch(7) == [6]


C like switch shortcut
----------------------

.. code-block:: python

   from switch import CSwitch
   # CSwitch(valk) is equvalent to Switch(val, fall_through=True)
