#!/usr/bin/env python2.7

from Tkinter import *
import tkMessageBox
# from RPi.GPIO import *
# # from wiringpi2 import *
from time import sleep

pinesGPIO = [2,3,4,17,27,22,10,9,11,14,15,18,23,24,25,8,7]
pinesGPIO

# setmode(BCM)
# setwarnings(False)

def stp(pin):
	setup(pin, OUT)

def on(pin):
    output(pin,1)


def off(pin):
    output(pin,0)


def repeat(pin,times):
    counter = 0
    while times >= counter:
        output(pin,1)
        sleep(.1)
        output(pin,0)
        sleep(.1)
        counter += 1


def OnButtonClick(button):
	result = tkMessageBox.askyesno("GPIO PIN","Do you want pin %s turn on?" % button)
	if result:
		stp(button)
		on(button)
	else:
		stp(button)
		repeat(button,4)
		off(button)



#Crea la ventana
raiz = Tk()

raiz.title('GPIO Pin')
raiz.geometry('180x550')

#Ventana
ventana = Frame(raiz)
ventana.grid(column=0, row=0, padx=(10,50), pady=(10,10))
ventana.columnconfigure(0,weight=1)
ventana.rowconfigure(0,weight=1)

#Etiquetas de texto
tag = Label(ventana, text="Pines")
tag.grid(column=2, row=1, pady=(5,5))

#------------Botones-----------#
def botonera():

    rowGrid = 2
    colGrid = 1

    # Primera columna

    for pin in pinesGPIO[:1+len(pinesGPIO)/2]:
        _ = Button(ventana, text=str(pin))
        _.grid(column=colGrid, row=rowGrid, padx=(5,5), pady=(5,5))
        _.config(command = lambda: OnButtonClick(pin))

        rowGrid += 1

    # Segunda columna

    colGrid = 3
    rowGrid = 2

    for pin in pinesGPIO[1+len(pinesGPIO)/2:]:
        _ = Button(ventana, text=str(pin))
        _.grid(column=colGrid, row=rowGrid, padx=(5,5), pady=(5,5))
        _.config(command = lambda: OnButtonClick(pin))

        rowGrid += 1

#------------------------------#

#Campo de entrada de texto
# entrada_txt = Entry(ventana, width=20, textvariable="")
# entrada_txt.grid(column=2, row=2)

#Poner en marcha el ciclo de eventos y llama a todas las funciones visuales
botonera()
raiz.mainloop()
