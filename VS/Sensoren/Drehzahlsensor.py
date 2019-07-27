import Sensor
import uuid
import random

class Drehzahlsensor(Sensor.Sensor):

    def __init__(self, sensorName):
        super().__init__(sensorName, "Drehzahlsensor")
        

    def simulieren(self):
        rnd = random.randint(0, 400)    
        return str(rnd)+" RPM"
