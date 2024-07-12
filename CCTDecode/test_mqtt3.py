import paho.mqtt.client as mqtt
MQTT_SERVER = "broker.hivemq.com"
MQTT_PATH = "/tide"
import numpy as np
import time
import cv2 as cv

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH)
    # The callback for when a PUBLISH message is received from the server.


def on_message(client, userdata, msg):
    # more callbacks, etc
    # Create a file with write byte permissi
    print("Image Received")
    print(msg.payload)
    nparr = np.frombuffer(msg.payload, np.uint8)
    img_np = cv.imdecode(nparr, cv.IMREAD_GRAYSCALE) # cv2.IMREAD_COLOR in OpenCV 3.1
    cv.imwrite('waka.jpg', img_np)

    cv.imshow('hey',img_np)
    time.sleep(1)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()