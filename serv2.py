# -*- coding: utf-8 -*-
from flask import Flask
import RPi.GPIO as GPIO
import time

# Configurar el sensor
GPIO.setmode(GPIO.BCM)

trig = 23
echo = 24

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
# -- Fin de la configuracion

app = Flask(__name__)

@app.route("/saludar")
def saludar():
	return "Hola"

@app.route("/ultra")
def ultra():
	GPIO.output(trig, GPIO.LOW)
	GPIO.output(trig, GPIO.HIGH)
	time.sleep(10 ** -4)
	GPIO.output(trig, GPIO.LOW)
	inicial = 0
	final = 0
	while GPIO.input(echo) == GPIO.LOW:
		inicial = time.time()
	while GPIO.input(echo) == GPIO.HIGH:
		final = time.time()
	duracion = final - inicial
	distancia = 171.5 * duracion
	return str(distancia * 100)

app.run(host="192.168.100.48")
#http://192.168.100.48:5000/saludar




