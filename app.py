from flask import Flask, render_template,redirect,request,url_for,session,g
from databases.database import *
from databases.measurements import *
import sys
import sqlite3

app = Flask(__name__)

app.secret_key = "secret_key"
tables = getAllTables()
@app.before_request
def before_request():
	g.db = sqlite3.connect("databases/measurements.db")

@app.teardown_request
def teardown_request(exception):
	if hasattr(g, "db"):
		g.db.close()

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/login", methods=["GET","POST"])
def login():
	error = None
	if request.method == "POST":
		if checkUser(request.form["username"],request.form["password"]) == False:
			error = "Invalid login credentials"
		else:
			session["logged_in"] = True
			session["username"] = request.form["username"]
			return redirect(url_for("dashboard"))
	return render_template("login.html",error=error)

@app.route("/dashboard")
def dashboard():
	if not session.get("logged_in"):
		return redirect(url_for("login"))
	else:
		current_table = getCurrentTable()
		time=g.db.execute("SELECT timestamp FROM "+current_table).fetchall()
		temp=g.db.execute("SELECT temperature FROM "+current_table).fetchall()
		hum=g.db.execute("SELECT humidity FROM "+current_table).fetchall()
		return render_template("dashboard.html",time=time,temp=temp,hum=hum)

@app.route("/history", methods=["GET", "POST"])
def history():
	option = request.form.get("options-form")
	#tables = getAllTables()

	return render_template("history.html",tables=tables)

@app.route("/display_history", methods=["GET", "POST"])
def display_history():
	option = request.form.get("options-form")
	time=g.db.execute("SELECT timestamp FROM "+option).fetchall()
	temp=g.db.execute("SELECT temperature FROM "+option).fetchall()	
	hum=g.db.execute("SELECT humidity FROM "+option).fetchall()    	
	avTemp = getAverage("temperature", option) 
	avHum = getAverage("humidity", option)

	return render_template("display_history.html",time=time,temp=temp,hum=hum,avTemp=avTemp,avHum=avHum,option=option)

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0")
