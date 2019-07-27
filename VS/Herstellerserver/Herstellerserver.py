import threading
import paho.mqtt.client as mqtt

class Herstellerserver(threading.Thread):

    def __init__(self):
         threading.Thread.__init__(self)
    
    def run(self):
        print("Herstellerserver gestartet...")
        running = True
        c = open("Sensordaten.txt", "w")
        c.close()
        broker_address="iot.eclipse.org" #broker address
        client = mqtt.Client("P2") #create new instance
        client.on_message=on_message #attach function to callback
        client.connect(broker_address) #connect to broker       
        client.loop_start()
        client.subscribe("SHZ")
        if (running == False):
            client.loop_stop()
        

def on_message(client, userdata, message):
    if (message.topic == "SHZ"):
        f = open("Sensordaten.txt", "a")
        f.write(data.decode())
        f.write("\n")
        f.close()
