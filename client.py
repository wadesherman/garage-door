import paho.mqtt.client as mqtt
import random

from time import sleep
from garagedoor import GarageDoor
from gd_io import IO
from mqttObserver import MqttObserver

def on_message(client, userdata, message):
    requested_state = str(message.payload.decode("utf-8"))

    if requested_state == 'open':
        print("requesting open")
        gd.request_open()

    if requested_state == 'closed':
        print("requestiong close")
        gd.request_closed()

    if requested_state == 'toggle':
        print("toggle")
        gd.toggle()

mqttc = mqtt.Client("MQTT_Client")
mqttc.connect("mq.casadeoso.com")
mqttc.subscribe("garage/door/status/set")
mqttc.on_message=on_message
mqttc.loop_start()

gd = GarageDoor(IO())

def main():
    while True:
        sleep(1)

main()
