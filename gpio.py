from RPi.GPIO import *

setmode(BCM)
setwarnings(False)

led = input("Escribe el pin: ")

setup(led, OUT)

onoff = raw_input("On or Off: ")

if onoff == "on":
        output(led, 1)
elif onoff == "off":
        output(led, 0)