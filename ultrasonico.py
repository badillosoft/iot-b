import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # GPIO.BOARD

trig = 23
echo = 24

# ajusta el sensor en el pin `trig` como salida
GPIO.setup(trig, GPIO.OUT)
# ajusta el sensor en el pin `echo` como entrada
GPIO.setup(echo, GPIO.IN)

# nos aseguramos que el sensor en `trig` se encuentre apagado
GPIO.output(trig, GPIO.LOW)

# lanzamos el pulso de disparo a `trig`
GPIO.output(trig, GPIO.HIGH)
time.sleep(10 ** -4)
GPIO.output(trig, GPIO.LOW)

inicial = 0
final = 0

# `echo` se encuentra en LOW

while GPIO.input(echo) == GPIO.LOW:
	inicial = time.time()

# `echo` se encuentra en HIGH

print("Se lanza el pulso en: {}".format(inicial))

while GPIO.input(echo) == GPIO.HIGH:
	final = time.time()

# `echo` se encuentra en LOW

print("Se acaba el pulso en: {}".format(final))

# calculamos la duracion del pulso en milisegundos
duracion = final - inicial

# v = d / t
# d = v * t
# d = (343000 * t) / 2
# d = 171500 * t

distancia = 171.5 * duracion

print("Distancia: {:.2f} cm".format(distancia * 100))

GPIO.cleanup()







