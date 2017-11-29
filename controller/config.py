def wifiConnect(ssid, passw):
	import network
	import utime
	netw = network.WLAN(network.STA_IF)
	if not netw.isconnected():
		netw.active(True)
		netw.connect(ssid, passw)
		while not netw.isconnected():
			utime.sleep_ms(20)
	
