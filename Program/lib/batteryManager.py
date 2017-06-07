import machine

class BatteryManager:
    numADCreadings = const(100)
    def __init__(self):
        self.adc = machine.ADC(0)
        self.adcread = self.adc.channel(attn=3, pin='P16')
        self.samplesADC = [0.0]*numADCreadings
        self.meanADC = 0.0

    def checkLowBattery(self):
        i = 0
        while (i < numADCreadings):
            adcint = self.adcread()
            self.samplesADC[i] = adcint
            self.meanADC += adcint
            i += 1

        self.meanADC /= numADCreadings
        voltage = (self.meanADC / 4096) * 3.548 / 0.3155
        if(voltage < 3.8):
            return True
        return False
