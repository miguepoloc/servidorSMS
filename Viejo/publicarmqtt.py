import paho.mqtt.publish as publish
import time
print("Enviando 0...")
publish.single("test", "0", hostname="127.0.0.1")
time.sleep(3)
print("Enviando 1...")
publish.single("test", "1", hostname="127.0.0.1")
