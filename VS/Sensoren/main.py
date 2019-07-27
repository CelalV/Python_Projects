import Temparatursensor
import Luftfeuchtigkeitssensor
import Drehzahlsensor
import Fensterzustandssensor
import uuid
import time


def main():
    
    luftfeuchtigkeitssensor = Luftfeuchtigkeitssensor.Luftfeuchtigkeitssensor(str(uuid.uuid4()))
    luftfeuchtigkeitssensor.start()

    fensterzustandssensor = Fensterzustandssensor.Fensterzustandssensor(str(uuid.uuid4()))
    fensterzustandssensor.start()

    drehzahlsensor = Drehzahlsensor.Drehzahlsensor(str(uuid.uuid4()))
    drehzahlsensor.start()

    temparatursensor = Temparatursensor.Temparatursensor(str(uuid.uuid4()))
    temparatursensor.start()

    #time.sleep(10)

    #luftfeuchtigkeitssensor.stop()
    #fensterzustandssensor.stop()
    #drehzahlsensor.stop()
    #temparatursensor.stop()

main()

