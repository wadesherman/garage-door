import paho.mqtt.client as mqtt
import random

from time import sleep
from garagedoor import GarageDoor
from gd_io import IO
from mqttObserver import MqttObserver

def on_message(client, userdata, message):
    requested_state = str(message.payload.decode("utf-8"))

    if requested_state == 'open':
        gd.request_open()

    if requested_state == 'closed':
        gd.request_closed()

    if requested_state == 'toggle':
        gd.toggle()

def on_connect(client, userdata, flags, rc):
    mqttc.subscribe("garage/door/status/set")

mqttc = mqtt.Client("MQTT_Client")
mqttc.on_connect=on_connect
mqttc.on_message=on_message
mqttc.connect("mq.casadeoso.com")
mqttc.loop_start()

gd = GarageDoor(IO())
gd.addObserver(MqttObserver(mqttc, "garage/door/status"))

def main():
    while True:
        sleep(1)

main()
