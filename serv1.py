# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

@app.route("/saludar")
def saludar():
	return "Hola"

app.run(host="192.168.100.48")
#http://192.168.100.48:5000/saludar
