import sqlite3
import os.path

database = "databases/measurements.db"

def createDB():
	conn = sqlite3.connect(database)
	db = conn.cursor()
	db.execute("""CREATE TABLE IF NOT EXISTS measurements 
			(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
			temperature TEXT NOT NULL,
			humidity Text NOT NULL)""")
	conn.commit()
	db.close()

def addMesurements(temperature, humidity):
	conn = sqlite3.connect(database)
	db = conn.cursor()
	db.execute("INSERT INTO measurements VALUES(?,?,?)",(None, temperature, humidity))
	conn.commit()
	db.close()

if os.path.exists(database) == False:
	createDB()
