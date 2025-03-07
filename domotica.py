
import paho.mqtt.client as mqtt

def accendi_luce():
    client = mqtt.Client()
    client.connect("mqtt.broker.address", 1883, 60)
    client.publish("casa/luce", "ON")
    client.disconnect()
