import sqlite3
import os.path
import datetime

database = "databases/measurements.db"
#table_name = datetime.date.today()
#table_name = str(table_name)
#table_name = str.replace(table_name, "-","_")
#table_name = "date_"+table_name
table_name = "kiriakos2"

av_tables = []

#print(table_name)
def createDB():
	conn = sqlite3.connect(database)
	db = conn.cursor()
	db.execute("""CREATE TABLE IF NOT EXISTS """+table_name +""" ( 
			timestamp TEXT NOT NULL,
			temperature TEXT NOT NULL,
			humidity TEXT NOT NULL)""")
	conn.commit()
	db.close()

def addMesurements(temperature, humidity):
	conn = sqlite3.connect(database)
	db = conn.cursor()
	db.execute("INSERT INTO "+ table_name +" VALUES(CURRENT_TIME,?,?)",(temperature, humidity))
	conn.commit()
	db.close()

def showAll():
	conn = sqlite3.connect("measurements.db")
	db = conn.cursor()
	db.execute("SELECT * FROM sqlite_master WHERE TYPE = 'table'")
	for name in db:
		print(name[1])
		av_tables.append(name[1])
	conn.commit()
	conn.close()

if os.path.exists(database) == False:
	createDB()
showAll()
