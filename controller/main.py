from config import wifiConnect
#from tempHum import temp_hum
from photoResistor import photo_resistor

while True:
	wifiConnect("danger-zone", "D3bianGnu0001lichessORG")
	#temp_hum()
	photo_resistor()
