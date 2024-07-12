import paho.mqtt.client as mqtt
import CCTDecodeRelease_light as cct
import time
import os
import cv2 as cv
import numpy as np

MQTT_SERVER = "broker.hivemq.com"
MQTT_PATH = "/tide"

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
    return img_np
    

def receive_mqtt():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_SERVER, 1883, 60)
    return client.on_message()



while True:
    raw_img = receive_mqtt()
    print(raw_img)
    t0 = time.perf_counter()
  

    code_table,processed_img=cct.CCT_extract(raw_img,12,0.85)
    #save_path=os.path.join(args.save_folder,args.filename)
    #cv.imwrite(save_path,processed_img)
    #        print(code_table)
    t1 = time.perf_counter()

    print('\n process time:',t1-t0)
    time.sleep(2)