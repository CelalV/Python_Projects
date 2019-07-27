import socket
import time
from datetime import datetime
import uuid
import random
import threading

class Sensor(threading.Thread):
    
    def __init__(self, sensorName, sensorTyp):
        self.sensorName = sensorName
        self.sensorTyp = sensorTyp
        threading.Thread.__init__(self)
        self.stop_threads = False

    def send(self, message):
        UDP_IP = "localhost"
        UDP_PORT = 1337
        now = datetime.now().strftime("%H:%M:%S")
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(str.encode(self.sensorName + "," + self.sensorTyp + "," + message +"," + datetime.now().strftime("%H:%M:%S %d/%m/%y")), (UDP_IP, UDP_PORT))


    def simulieren(self):
        pass
    
    def run(self):
        print(self.sensorTyp + " wurde gestartet...\n")
        while True:
            self.send(self.simulieren())
            time.sleep(1)
            if self.stop_threads:
                break

    def stop(self):
        self.stop_threads = True

