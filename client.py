import paho.mqtt.client as mqtt
import random
import os
from time import sleep
from dotenv import load_dotenv

from garagedoor import GarageDoor
from gd_io import IO
from mqttObserver import MqttObserver

load_dotenv(override=True)

def on_message(client, userdata, message):
    requested_state = str(message.payload.decode("utf-8"))

    if requested_state == 'open':
        gd.request_open()

    if requested_state == 'closed':
        gd.request_closed()

    if requested_state == 'toggle':
        gd.toggle()

def on_connect(client, userdata, flags, rc):
    mqttc.subscribe(os.getenv("COMMAND_TOPIC"))

mqttc = mqtt.Client("MQTT_Client")
mqttc.on_connect=on_connect
mqttc.on_message=on_message
mqttc.connect(os.getenv("MQ_BROKER"))
mqttc.loop_start()

gd = GarageDoor(IO())
gd.addObserver(MqttObserver(mqttc, os.getenv("STATE_TOPIC")))

def main():
    epic = True
    while epic:
        sleep(1)

main()
