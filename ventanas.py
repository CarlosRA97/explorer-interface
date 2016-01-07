from Tkinter import *
from RPi.GPIO import *

lista = [2,3,4,17,27,22,10,9,11,14,15,18,23,24,25,8,7]


setmode(BCM)
setwarnings(False)

def onoff(pin):
	int(pin)
	print pin




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
tag.grid(column=1, row=1, pady=(5,5))

#Botones

# Primera columna
button3v3 = Button(ventana, text="3v3")
button3v3.grid(column=1, row=2, padx=(5,5), pady=(5,5))

button2 = Button(ventana, text="2", command = onoff(button2["text"]))
button2.grid(column=1, row=3, padx=(5,5), pady=(5,5))

button3 = Button(ventana, text="3", command = onoff(button3["text"]))
button3.grid(column=1, row=4, padx=(5,5), pady=(5,5))

button4 = Button(ventana, text="4", command = onoff(button4["text"]))
button4.grid(column=1, row=5, padx=(5,5), pady=(5,5))

buttongnd = Button(ventana, text="GND")
buttongnd.grid(column=1, row=6, padx=(5,5), pady=(5,5))

button17 = Button(ventana, text="17", command = onoff(button17["text"]))
button17.grid(column=1, row=7, padx=(5,5), pady=(5,5))

button27 = Button(ventana, text="27", command = onoff(button27["text"]))
button27.grid(column=1, row=8, padx=(5,5), pady=(5,5))

button22 = Button(ventana, text="22", command = onoff(button22["text"]))
button22.grid(column=1, row=9, padx=(5,5), pady=(5,5))

button3v32 = Button(ventana, text="3v3")
button3v32.grid(column=1, row=10, padx=(5,5), pady=(5,5))

button10 = Button(ventana, text="10", command = onoff(button10["text"]))
button10.grid(column=1, row=11, padx=(5,5), pady=(5,5))

button9 = Button(ventana, text="9", command = onoff(button9["text"]))
button9.grid(column=1, row=12, padx=(5,5), pady=(5,5))

button11 = Button(ventana, text="11", command = onoff(button11["text"]))
button11.grid(column=1, row=13, padx=(5,5), pady=(5,5))

buttongnd2 = Button(ventana, text="GND")
buttongnd2.grid(column=1, row=14, padx=(5,5), pady=(5,5))


# Segunda columna

button5v = Button(ventana, text="5v")
button5v.grid(column=2, row=2, padx=(5,5), pady=(5,5))

button5v2 = Button(ventana, text="5v")
button5v2.grid(column=2, row=3, padx=(5,5), pady=(5,5))

buttongnd3 = Button(ventana, text="GND")
buttongnd3.grid(column=2, row=4, padx=(5,5), pady=(5,5))

button14 = Button(ventana, text="14", command = onoff(button14["text"]))
button14.grid(column=2, row=5, padx=(5,5), pady=(5,5))

button15 = Button(ventana, text="15", command = onoff(button15["text"]))
button15.grid(column=2, row=6, padx=(5,5), pady=(5,5))

button18 = Button(ventana, text="18", command = onoff(button18["text"]))
button18.grid(column=2, row=7, padx=(5,5), pady=(5,5))

buttongnd4 = Button(ventana, text="GND")
buttongnd4.grid(column=2, row=8, padx=(5,5), pady=(5,5))

button23 = Button(ventana, text="23", command = onoff(button23["text"]))
button23.grid(column=2, row=9, padx=(5,5), pady=(5,5))

button24 = Button(ventana, text="24", command = onoff(button24["text"]))
button24.grid(column=2, row=10, padx=(5,5), pady=(5,5))

buttongnd5 = Button(ventana, text="GND")
buttongnd5.grid(column=2, row=11, padx=(5,5), pady=(5,5))

button25 = Button(ventana, text="25", command = onoff(button25["text"]))
button25.grid(column=2, row=12, padx=(5,5), pady=(5,5))

button8 = Button(ventana, text="8", command = onoff(button8["text"]))
button8.grid(column=2, row=13, padx=(5,5), pady=(5,5))

button7 = Button(ventana, text="7", command = onoff(button7["text"]))
button7.grid(column=2, row=14, padx=(5,5), pady=(5,5))





#Campo de entrada de texto
# entrada_txt = Entry(ventana, width=20, textvariable="")
# entrada_txt.grid(column=2, row=2)

#Poner en marcha el ciclo de eventos
raiz.mainloop()
