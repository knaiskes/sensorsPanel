def wifiConnect(ssid, passw):
	import network
	netw = network.WLAN(network.STA_IF)
	if not netw.isconnected():
		netw.active(True)
		netw.connect(ssid, passw)
		while not netw.isconnected():
			pass
	
