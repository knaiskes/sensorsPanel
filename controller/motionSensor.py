from mqtt.simple import MQTTClient
from time import sleep
import micropython
from machine import Pin


# MQTT
SERVER = b"192.168.2.3" # Raspberry Pi with static IP address 
CLIENT_ID = b"esp_motion_sensor"
TOPIC = b"motionSensor"

sensor = Pin(5, Pin.IN)
led = Pin(2, Pin.OUT)

def motion_sensor():
	client = MQTTClient(CLIENT_ID, SERVER)
	client.connect()

	while True:
		try:
			if sensor.value() == 1:
				led.value(1)
				msg = "motion"
				client.publish(TOPIC, msg)
			else:
				led.value(0)
		except OSError:
			print("System Error")
		# sleep(3600) # one hour
		sleep(10) # for testing
