from RPi.GPIO import *
from time import sleep

setmode(BCM)
setwarnings(False)

pin = raw_input("pin?: ")
led = int(pin)
setup(led, OUT)

onoff = raw_input("On or Off: ")

if onoff == "on":
	output(led, 1)
elif onoff == "off":
	output(led, 0)
