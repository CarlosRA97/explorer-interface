from Tkinter import *
import tkMessageBox
from RPi.GPIO import *

lista = [2,3,4,17,27,22,10,9,11,14,15,18,23,24,25,8,7]


setmode(BCM)
setwarnings(False)

def onoff(pin):
	print pin

def OnButtonClick(self, button):
	print buttonself.
	tkMessageBox.showinfo("You clicked the pin")



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

self.button2 = Button(self,ventana, text="2|SDA")
self.button2.grid(column=1, row=3, padx=(5,5), pady=(5,5))
self.button2.config(command = lambda button=button2: self.OnButtonClick(button))

self.button3 = Button(self,ventana, text="3|SCL")
self.button3.grid(column=1, row=4, padx=(5,5), pady=(5,5))
self.button3.config(command = lambda button=button3: self.OnButtonClick(button))

self.button4 = Button(self,ventana, text="4")
self.button4.grid(column=1, row=5, padx=(5,5), pady=(5,5))
self.button4.config(command = lambda button=button4: self.OnButtonClick(button))

buttongnd = Button(ventana, text="GND")
buttongnd.grid(column=1, row=6, padx=(5,5), pady=(5,5))

self.button17 = Button(self,ventana, text="17")
self.button17.grid(column=1, row=7, padx=(5,5), pady=(5,5))
self.button17.config(command = lambda button=button17: self.OnButtonClick(button))

self.button27 = Button(self,ventana, text="27")
self.button27.grid(column=1, row=8, padx=(5,5), pady=(5,5))
self.button27.config(command = lambda button=button27: self.OnButtonClick(button))

self.button22 = Button(self,ventana, text="22")
self.button22.grid(column=1, row=9, padx=(5,5), pady=(5,5))
self.button22.config(command = lambda button=button22: self.OnButtonClick(button))

button3v32 = Button(ventana, text="3v3")
button3v32.grid(column=1, row=10, padx=(5,5), pady=(5,5))

self.button10 = Button(self,ventana, text="10|MOSI")
self.button10.grid(column=1, row=11, padx=(5,5), pady=(5,5))
self.button10.config(command = lambda button=button10: self.OnButtonClick(button))

self.button9 = Button(self,ventana, text="9|MISO")
self.button9.grid(column=1, row=12, padx=(5,5), pady=(5,5))
self.button9.config(command = lambda button=button9: self.OnButtonClick(button))

self.button11 = Button(self,ventana, text="11|SCLK")
self.button11.grid(column=1, row=13, padx=(5,5), pady=(5,5))
self.button11.config(command = lambda button=button11: self.OnButtonClick(button))

buttongnd2 = Button(ventana, text="GND")
buttongnd2.grid(column=1, row=14, padx=(5,5), pady=(5,5))


# Segunda columna

button5v = Button(ventana, text="5v")
button5v.grid(column=2, row=2, padx=(5,5), pady=(5,5))

button5v2 = Button(ventana, text="5v")
button5v2.grid(column=2, row=3, padx=(5,5), pady=(5,5))

buttongnd3 = Button(ventana, text="GND")
buttongnd3.grid(column=2, row=4, padx=(5,5), pady=(5,5))

self.button14 = Button(self,ventana, text="14|TXD")
self.button14.grid(column=2, row=5, padx=(5,5), pady=(5,5))
self.button14.config(command = lambda button=button14: self.OnButtonClick(button))

self.button15 = Button(self,ventana, text="15|RXD")
self.button15.grid(column=2, row=6, padx=(5,5), pady=(5,5))
self.button15.config(command = lambda button=button15: self.OnButtonClick(button))

self.button18 = Button(self,ventana, text="18")
self.button18.grid(column=2, row=7, padx=(5,5), pady=(5,5))
self.button18.config(command = lambda button=button18: self.OnButtonClick(button))

buttongnd4 = Button(ventana, text="GND")
buttongnd4.grid(column=2, row=8, padx=(5,5), pady=(5,5))

self.button23 = Button(self,ventana, text="23")
self.button23.grid(column=2, row=9, padx=(5,5), pady=(5,5))
self.button23.config(command = lambda button=button23: self.OnButtonClick(button))

self.button24 = Button(self,ventana, text="24")
self.button24.grid(column=2, row=10, padx=(5,5), pady=(5,5))
self.button24.config(command = lambda button=button24: self.OnButtonClick(button))

buttongnd5 = Button(ventana, text="GND")
buttongnd5.grid(column=2, row=11, padx=(5,5), pady=(5,5))

self.button25 = Button(self,ventana, text="25")
self.button25.grid(column=2, row=12, padx=(5,5), pady=(5,5))
self.button25.config(command = lambda button=button25: self.OnButtonClick(button))

self.button8 = Button(self,ventana, text="8|CE0")
self.button8.grid(column=2, row=13, padx=(5,5), pady=(5,5))
self.button8.config(command = lambda button=button8: self.OnButtonClick(button))

self.button7 = Button(self,ventana, text="7|CE127")
self.button7.grid(column=2, row=14, padx=(5,5), pady=(5,5))
self.button7.config(command = lambda button=button7: self.OnButtonClick(button))



#Campo de entrada de texto
# entrada_txt = Entry(ventana, width=20, textvariable="")
# entrada_txt.grid(column=2, row=2)

#Poner en marcha el ciclo de eventos
raiz.mainloop()
