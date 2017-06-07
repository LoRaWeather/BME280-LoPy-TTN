from lopyConstants import *
from network import LoRa
import binascii
import pycom
import struct
import machine
import time
import socket

class LoraConnection:
    def __init__(self):
        pycom.heartbeat(False)
        self.lora = LoRa(mode=LoRa.LORAWAN)

        self.app_eui = binascii.unhexlify(app_eui)
        self.app_key = binascii.unhexlify(app_key)

        pycom.rgbled(red)

    def connectToTTN(self):
        self.lora.join(activation=LoRa.OTAA, auth=(self.app_eui, self.app_key), timeout=0)
        # Loop until joined
        while not self.lora.has_joined():
            print('Not joined yet...')
            pycom.rgbled(off)
            time.sleep(0.1)
            pycom.rgbled(red)
            time.sleep(2)
        print('Joined')
        pycom.rgbled(blue)
        self._createSocket()
        return True

    def _createSocket(self):
        self.socket = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
        self.socket.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
        self.socket.setblocking(True)

    def sendData(self, version, temperature, humidity, pressure):
        print(version + ' ' + temperature + ' ' + humidity + ' ' + pressure)
        self.setEncodedData(temperature, humidity, pressure)
        data = struct.pack(">hhbb", self.temperature, self.pressure, self.humidity, int(version))
        self.socket.send(data)
        print('Data send: ' + str(data))
        pycom.rgbled(green)
        time.sleep(0.1)
        pycom.rgbled(blue)
        time.sleep(10)
        #machine.deepsleep(900000)

    def setEncodedData(self, temperature, humidity, pressure):
        temperature = int(float(temperature)*100)
        if(temperature < 0):
            temperature = ~temperature
            temperature += temperaturemask # 1 + 32768 (10000000 00000000)
        self.temperature = temperature

        self.humidity = int(float(humidity))

        self.pressure = int(float(pressure)*10)
