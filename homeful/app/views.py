from app import app
from flask import render_template,request
import math
from sympy import *
import locale
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'Tics2'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456789tics'
app.config['MYSQL_DATABASE_DB'] = 'Tics2'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn = mysql.connect()
cur = conn.cursor()

locale.setlocale(locale.LC_ALL,'en_US.utf-8')



@app.route('/', methods=["POST", "GET"])
def index():

	sql="select * from publicacion;"
	cur.execute(sql)
	publicaciones=cur.fetchall()

	return render_template("indexprueba.html", publicaciones=publicaciones)

@app.route('/index', methods=["POST", "GET"])
def index2():

	sql="select * from publicacion;"
	cur.execute(sql)
	publicaciones=cur.fetchall()

	return render_template("indexprueba.html", publicaciones=publicaciones)


@app.route('/about', methods=["POST", "GET"])
def about():

	return render_template("about.html")

@app.route('/agents', methods=["POST", "GET"])
def agents():

	return render_template("agents.html")

@app.route('/avisopropiedad', methods=["POST", "GET"])
def avisopropiedad():

	return render_template("avisopropiedad.html")

@app.route('/blog-home', methods=["POST", "GET"])
def bloghome():

	return render_template("blog-home.html")

@app.route('/contact', methods=["POST", "GET"])
def contact():

	return render_template("contact.html")

@app.route('/properties', methods=["POST", "GET"])
def properties():

	return render_template("properties.html")