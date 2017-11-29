from config import wifiConnect
#from tempHum import temp_hum
#from photoResistor import photo_resistor
from motionSensor import motion_sensor

while True:
	wifiConnect("", "")
	#temp_hum()
	#photo_resistor()
	motion_sensor()
