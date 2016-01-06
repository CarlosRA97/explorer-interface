from RPi.GPIO import *
<<<<<<< HEAD
from ventanas import Ventana
=======
from time import sleep
>>>>>>> origin/master

# setmode(BCM)
# setwarnings(False)

<<<<<<< HEAD
# led = input("Escribe el pin: ")

# setup(led, OUT)
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

ventana1 = Ventana()

ventana1.w()
=======
if onoff == "on":
	output(led, 1)
elif onoff == "off":
	output(led, 0)
>>>>>>> origin/master
