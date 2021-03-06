from flask import Flask
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

app = Flask(__name__)

pines = [24, 23, 22, 27, 17, 18]

for pin in pines:
	GPIO.setup(pin, GPIO.OUT)

@app.route("/led/<int:id>/on")
def led_on(id):
	pin = pines[id]
	GPIO.output(pin, GPIO.HIGH)
	return "pin {} ({}) encendido".format(id, pin)

@app.route("/led/<int:id>/off")
def led_off(id):
	pin = pines[id]
        GPIO.output(pin, GPIO.LOW)
        return "pin {} ({}) apagado".format(id, pin)

app.run(port = 80)

