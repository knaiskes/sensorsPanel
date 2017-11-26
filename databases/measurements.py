import sqlite3
import os.path
import datetime

database = "databases/measurements.db"
table_name = datetime.date.today()
table_name = str(table_name)
table_name = str.replace(table_name, "-","_")
table_name = "date_"+table_name

av_tables = []

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
	db.execute("""CREATE TABLE IF NOT EXISTS """+table_name +""" ( 
			timestamp TEXT NOT NULL,
			temperature TEXT NOT NULL,
			humidity TEXT NOT NULL)""")

	db.execute("INSERT INTO "+ table_name +" VALUES(CURRENT_TIME,?,?)",(temperature, humidity))
	conn.commit()
	db.close()

def getAllTables():
	conn = sqlite3.connect(database)
	db = conn.cursor()
	db.execute("SELECT * FROM sqlite_master WHERE TYPE = 'table'")
	for name in db:
		#print(name[1])
		av_tables.append(name[1])
	conn.commit()
	conn.close()
	return av_tables

def getCurrentTable():
	latest_table = []
	conn = sqlite3.connect(database)
	db = conn.cursor()
	db.execute("SELECT * FROM sqlite_master WHERE TYPE = 'table'")
	for name in db:
		latest_table.append(name[1])
	conn.commit()
	conn.close()
	return latest_table[-1]
		
def getAverage(operation,table):
	sumUp =0
	length = 0
	conn = sqlite3.connect(database)
	db = conn.cursor()
	db.execute("SELECT "+operation +" FROM "+table)
	for v in db:
		num = v[0]
		num = float(num)
		sumUp = sumUp + num
		length = length + 1
	sumUp = sumUp / length
	conn.commit()
	db.close()
	return round(sumUp,2)

if os.path.exists(database) == False:
	createDB()
