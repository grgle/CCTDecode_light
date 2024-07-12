import time

from compas_eve import Subscriber
from compas_eve import Topic
from compas_eve.mqtt import MqttTransport

from compas_eve.mqtt

topic = Topic("/tide")
tx = MqttTransport("broker.hivemq.com")

subcriber = Subscriber(topic, callback=lambda msg: print(f"Received message: {msg}"), transport=tx)
subcriber.subscribe()

print("Waiting for messages, press CTRL+C to cancel")
while True:
    time.sleep(1)