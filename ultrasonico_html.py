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
while GPIO.input(echo) == GPIO.HIGH:
	final = time.time()

# `echo` se encuentra en LOW

# calculamos la duracion del pulso en milisegundos
duracion = final - inicial

# v = d / t
# d = v * t
# d = (343000 * t) / 2
# d = 171500 * t

distancia = 171.5 * duracion

html = """
<!DOCTYPE html>
<html>
<head>
  <meta charset='utf-8'>
  <title>Sensor Ultrasonico</title>
  <style>
    * {
      margin: 0px;
      padding: 0px;
      box-sizing: border-box;
    }
    .app {
      position: absolute;
      display: flex;
      justify-content: center;
      align-items: center;
      width: 100%;
      height: 100%;
      background-color: rgba(0, 0, 255, 0.3);
    }
    .caja {
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 20px;
      background-color: cornflowerblue;
      border-radius: 10px;
      box-shadow: 0px 0px 4px 4px rgba(127, 127, 127, 0.5); 
    }
  </style>
</head>
<body>
  <div class='app'>
    <div class='caja'>
      <h1>Distancia: @@</h1>
    </div>
  </div>
</body>
</html>
""".replace("@@", str(distancia * 100))

print(html)

GPIO.cleanup()







