from lopyConstants import *
from machine import I2C
from BME280 import *
from BatteryManager import *
from LoraConnection import LoraConnection
import time
import struct
import pycom

# Turn off hearbeat LED
pycom.heartbeat(False)

# init classes
i2c = I2C(0, I2C.MASTER, baudrate=400000)
sensor = BME280(address=BME280_I2CADDR, i2c=i2c)
connection = LoraConnection()
connected = connection.connectToTTN()
batteryMngr = BatteryManager()

while True:
    print('start')
    if(batteryMngr.checkLowBattery()):
        print('Battery is below 25%')
        version = version | batterymask
    if(connected):
        connection.sendData(version, sensor.temperature, sensor.humidity, sensor.pressure)
    print('end')
