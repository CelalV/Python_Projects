import Sensor
import uuid
import random

class Luftfeuchtigkeitssensor(Sensor.Sensor):

    def __init__(self, sensorName):
        super().__init__(sensorName, "Luftfeuchtigkeitssensor")


    def simulieren(self):
        rnd = random.randint(20, 80)
        return str(rnd) + " %"
