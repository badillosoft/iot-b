# -*- coding: utf-8 -*-
from flask import Flask
import os
import json

app = Flask(__name__)

@app.route("/saludar")
def saludar():
	return "Hola"

@app.route("/ultra")
def ultra():
	stream = os.popen("python ultrasonico.py")
	return json.dumps(stream.read().split("\n"))

app.run(host="192.168.100.48")
#http://192.168.100.48:5000/saludar




