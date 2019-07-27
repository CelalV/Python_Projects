import Sensor
import uuid
import random

class Fensterzustandssensor(Sensor.Sensor):

    def __init__(self, sensorName):
        super().__init__(sensorName, "Fensterzustandssensor")


    def simulieren(self):
        rnd = random.randint(0,1)
        if (rnd == 0):
            return "Geschlossen"
        else:
            return "Geoeffnet"
