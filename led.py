import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pines = [24, 23, 22, 27, 17, 18]

for pin in pines:
	GPIO.setup(pin, GPIO.OUT)

# Encender cada pin hacia enfrente
for pin in pines:
	GPIO.output(pin, GPIO.HIGH)
	time.sleep(0.2)
	GPIO.output(pin, GPIO.LOW)

# Encender cada pin al reves
for pin in pines[::-1]:
	GPIO.output(pin, GPIO.HIGH)
	time.sleep(0.2)
	GPIO.output(pin, GPIO.LOW)

GPIO.cleanup()	
