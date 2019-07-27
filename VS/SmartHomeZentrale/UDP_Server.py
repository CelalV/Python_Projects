import socket
import threading
import paho.mqtt.client as mqtt

class UDPServer(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        print("UDP Server gestartet...\n")
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('localhost', 1337))
        c = open("Sensordaten.txt", "w")
        c.close()
        client = mqtt.Client("P1")
        broker_address="iot.eclipse.org"
        client.connect(broker_address)
        
        while True:
            f = open("Sensordaten.txt", "a")
            data, adress = sock.recvfrom(1024)
            print(data.decode())
            f.write(data.decode())
            f.write("\n")
            f.close()
            client.publish("SHZ", data.decode())
