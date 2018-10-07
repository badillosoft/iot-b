from flask import Flask
import RPi.GPIO as GPIO
import os

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

stack = []
MAX_STACK = 100
id = "mossier-baboon-6494"

neighbors = ["accumbent-emu-7149", "magmatic-kudo-8520"]

@app.route("/message/<id_m>/<id_n>/<cmd>")
def message(id_m, id_n, cmd):
	print("recibiendo {} {} {}".format(id_m, id_n, cmd))
	# Para cada id_x (el id del mensaje en el stack)
	for id_x in stack:
		# Si el mensaje que recibe ya esta en el stack finaliza
		if id_m == id_x:
			print("nothing")
			return "done [nothing]"
	# Si el id del nodo es igual al id de este nodo
	if id_n == id:
		# Convierto el comando a / (ej. led-3-on => led/3/on)
		cmd = cmd.replace("-", "/")
		# Ejecuto el comando
		os.system("curl https://{}.dataplicity.io/{}".format(id, cmd))
		print("exec")
		return "done [self]"
	# Si el stack supera el numero maximo
	if len(stack) > MAX_STACK:
		# Elimina el primer mensaje
		stack.pop(0)
	# Guardar el id del mensaje en el stack
	stack.append(id_m)
	# Replicar el mensaje a los vecinos
	for id_y in neighbors:
		os.system("curl https://{}.dataplicity.io/message/{}/{}/{}".format(id_y, id_m, id_n, cmd))
		print("transmitiendo {}".format(id_y))
	return "done [replicate]"
	
app.run(port = 80)

