from transitions import Machine
from time import sleep

class GarageDoor(object):

    observers = []
    states = ['open', 'transitioning', 'closed']
    io = None

    def addObserver(self, observer):
        self.observers.append(observer)

    def __init__(self, io):
        self.io = io

        self.machine = Machine(
            model=self,
            states=self.states,
            initial=self.getDoorState(),
            ignore_invalid_triggers=True,
        )

        self.machine.add_transition(trigger='request_open', source='closed', dest='transitioning')
        self.machine.add_transition(trigger='request_closed', source='open', dest='transitioning')
        self.machine.add_transition(trigger='toggle', source=['open', 'closed'], dest='transitioning')
        self.machine.add_transition(trigger='resolve_closed', source='transitioning', dest='closed', after='notify')
        self.machine.add_transition(trigger='resolve_open', source='transitioning', dest='open', after='notify')

        self.machine.on_enter_transitioning('pressButton')

    def pressButton(self):
        self.io.pressButton()
        sleep(3)
        self.resolveDoorState()

    def resolveDoorState(self):
        self.resolve_closed() if self.isClosed() else self.resolve_open()

    def getDoorState(self):
        return 'closed' if self.isClosed() else 'open'

    def isClosed(self):
        return self.io.isClosed()

    def notify(self):
        for o in self.observers:
            o.notify(self.state)

class Foo:
    def pressButton(self):
        print('pressButton')

    def isClosed(self):
        print('isClosed')
