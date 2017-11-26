from config import wifiConnect
#from tempHum import temp_hum
from photoResistor import photo_resistor

while True:
	wifiConnect("", "")
	#temp_hum()
	photo_resistor()
