import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

ch1 = 23
ch2 = 24

GPIO.setup(ch1, GPIO.OUT)
GPIO.setup(ch2, GPIO.OUT)

GPIO.output(ch1, GPIO.HIGH)
time.sleep(5)
GPIO.output(ch1, GPIO.LOW)

GPIO.cleanup()
