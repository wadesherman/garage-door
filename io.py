from gpiozero import OutputDevice
from gpiozero import Button
from time import sleep

class IO:

    def __init__(self):
        self.foo = OutputDevice(19, initial_value=True)
        self.relay = OutputDevice(27)
        self.sensor = Button(13, pull_up=None)

    def isClosed(self):
        return self.sensor.is_pressed

    def pressButton(self):
        self.relay.on()
        sleep(1)
        self.relay.off()
        sleep(1)
