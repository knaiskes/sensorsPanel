import paho.mqtt.client as mqtt
from databases.measurements import *

# import from db file

def on_connect(client, userdata, flags, rc):
	print("Connected with result code {0}".format(rc))
	client.subscribe("tempSensor")

def on_message(client, userdata, msg):
	t,h = [float(x) for x in msg.payload.decode("utf-8").split(",")]
	print("{0}*C {1}%".format(t,h))
	addMesurements(t, h)

#	conn = sqlite3.connect(database)
#	db = conn.cursor()
#	db.execute("INSERT INTO users VALUES(?,?,?)",(None, t, h))
#	conn.commit()
#	db.close()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)

client.loop_forever()
