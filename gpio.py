from RPi.GPIO import *
from time import sleep

setmode(BCM)
setwarnings(False)

led = input("Escribe el pin: ")

setup(led, OUT)
=======
pin = raw_input("pin?: ")
led = int(pin)
setup(led, OUT)
>>>>>>> origin/master

# onoff = raw_input("On or Off: ")

<<<<<<< HEAD
# if onoff == "on":
#         output(led, 1)
# elif onoff == "off":
#         output(led, 0)

=======
if onoff == "on":
	output(led, 1)
elif onoff == "off":
	output(led, 0)
>>>>>>> origin/master
