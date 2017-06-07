# BME280-LoPy-TTN
This repository is for the program on the LoPy. The LoPy will read data from the BME280 sensor and send it to The Things Network over LoRa. The repository exists of two folders, Program and Documentation. The Program folder contains the whole program that is on the LoPy.


## Contents
1. Program
2. Documentation
3. Links

### Program
The program reads data from the BME280 sensor. This is a sensor that returns temperature, humidity and pressure data. The LoPy will send de data to The Things Network over LoRa. It uses OTAA (Over The Air Activation). The device has to be registered on The Things Network website. Once registered the user has to change two variables. In the lib folder there is a file called lopyConstants.py. In this file the user has to change the app_eui and the app_key that are identical to The Things Network.

The program can be uploaded to the LoPy after changing those variables. After a reset the LoPy will start sending data to The Things Network. Right now this is every 10 seconds, used for testing.

### Documentation
The program is fully documented. The documentation is generated in the Documentation folder. This is done by using Sphinx for Python.

To take a look at the documentation you have to go into the Documentation folder and navigate into \_build/hmtl folder. In that folder you will find the index.html file. Opening that file will open the homepage of the documentation.

If there are changes being made to the program you also have to change the documentation. This can be done by opening the [filename].rst files and change whatever you have changed. After changing those files you have to navigate to the Documentation folder with a command line tool. Once you are in that folder you have to execute the following command:
```
make html
```
This will generate the newly made documentation.

### Links
[Pycom LoPy](https://www.pycom.io/product/lopy/) </br>
[BME280 sensor](https://learn.adafruit.com/adafruit-bme280-humidity-barometric-pressure-temperature-sensor-breakout/overview)</br>
[The Things Network](https://www.thethingsnetwork.org/)</br>
[Sphinx python documentation generator](http://www.sphinx-doc.org/en/stable/)
