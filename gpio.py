from RPi.GPIO import *
from ventanas import Ventana

# setmode(BCM)
# setwarnings(False)

# led = input("Escribe el pin: ")

# setup(led, OUT)

# onoff = raw_input("On or Off: ")

# if onoff == "on":
#         output(led, 1)
# elif onoff == "off":
#         output(led, 0)

ventana1 = Ventana()

ventana1.w()