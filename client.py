import paho.mqtt.client as mqtt
import random
from time import sleep

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

mqttc = mqtt.Client("MQTT_Client")
mqttc.connect("")
mqttc.subscribe("sometopic")
mqttc.on_message=on_message
mqttc.loop_start()

while True:
    temperature = random.randint(1,101)
    mqttc.publish("paho/temperature", temperature)
    sleep(10)
