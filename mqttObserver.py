class MqttObserver:

    def __init__(self, client, topic):
        self.client = client
        self.topic = topic

    def notify(self, state):
        self.client.publish(self.topic, state, 0, True)
