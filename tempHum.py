from umqtt.simple import MQTTClient
from machine import Pin
import micropython
from time import sleep
from dht import DHT22

# MQTT
SERVER = "192.168.2.3" # Raspberry Pi
CLIENT_ID = "esp_dht22_sensor"
TOPIC = b"tempSensor"

sensor = Pin(5, Pin.IN, Pin.PULL_UP))

while True:
	try:
		sensor.measure()
		temperature = sensor.temperature()
		humidity = sensor.humidity()
		if isinstance(temperature, float) and isinstance(humidity, float):
			msg = (b "{0:3.1f},{1:3.1f}".format(temperature, humidity))
			print(msg) # to be removed later
			client.publish(TOPIC, msg)
	except OSError:
		print("System error")
	# sleep(3600) # one hour
	sleep(10) # for testing
