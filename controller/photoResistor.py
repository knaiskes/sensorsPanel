from umqtt.simple import MQTTClient
from machine import ADC
from time import sleep
import micropython


# MQTT
SERVER = b"192.168.2.3" # Raspberry Pi with static IP address 
CLIENT_ID = b"esp_photo_sensor"
TOPIC = b"photoSensor"

def photo_resistor():
	client = MQTTClient(CLIENT_ID, SERVER)
	client.connect()
	sensor = ADC(0)

	while True:
		try:
			value = sensor.read()
			if isinstance(value, int):
				value = str(value)
				msg = value
				print("Message:",msg)
				client.publish(TOPIC, msg)
		except OSError:
			print("System Error")
		# sleep(3600) # one hour
		sleep(10) # for testing
