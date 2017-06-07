LoraConnection
==============
On this page you will find the class defenition of the class LoraConnection

Functions
---------
.. class:: LoraConnection

   With this class you can connect and send to The Things Network.

.. function:: __init__()
  :noindex:

  Initialize lora variable with the app eui and key.

.. function:: connectToTTN()

   Sends a join request to the TTN.
   Keeps trying until connected. After that the method _createCocket() is called.

.. function:: _creatSocket()

   Creates a socket. Data can be send using the socket.

.. function:: setEncodeData(temperature, humidity, pressure)

   Sets the give data. Checks whether the temperature is negative.
   Creates int of the data types so the total send data will be minimalized.

   :param temperature: Temperature data
   :type temperature: Decimal number as a string
   :param humidity: Humidity data
   :type humidity: Number as a string
   :param pressure: Pressure data
   :type pressure: Decimal number as a string

.. function:: sendData(version, temperature, humidity, pressure)

   Packs the data to one objects and sends it to The Things Network.
   After that the LoPy will sleep for one hour and repeats the whole process.

   :param version: Version of device
   :type version: Int
   :param temperature: Temperature data
   :type temperature: Decimal number as a string
   :param humidity: Humidity data
   :type humidity: Number as a string
   :param pressure: Pressure data
   :type pressure: Decimal number as a string

Source
------
This is the source code of the class LoraConnection.py

.. literalinclude:: ..\Program\lib\LoraConnection.py
