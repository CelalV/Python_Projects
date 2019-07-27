import Sensor
import uuid
import random


class Temparatursensor(Sensor.Sensor):

    def __init__(self, sensorName):
        super().__init__(sensorName, "Temparatursensor")


    def simulieren(self):
        rnd = random.randint(12, 32)
        return str(rnd)+ " C"
