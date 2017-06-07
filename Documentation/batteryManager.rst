batteryManager
==============
On this page you will find the class defenition of the class batteryManager

Functions
---------
.. class:: batteryManager

   With this class you can read the battery value.
   The battery value is read by an adc pin on the LoPy.

.. function:: __init__()

   Initialize adc variable and reading values.

.. function:: checkLowBattery()

   Reads the adc value 100 times and gets the mean of it.
   If the value is below 3.8 the battery is below 25% of capacity, this will return true.
   3.8 = 25% and 4.2 = 100%.

Source
------
This is the source code of the class batteryManager.py

.. literalinclude:: ..\Program\lib\batteryManager.py
