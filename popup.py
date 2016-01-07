from Tkinter import *
import tkMessageBox

raiz = Tk()

raiz.title('GPIO Pin')
raiz.geometry('180x550')

#Ventana
ventana = Frame(raiz)
ventana.grid(column=0, row=0, padx=(10,50), pady=(10,10))
ventana.columnconfigure(0,weight=1)
ventana.rowconfigure(0,weight=1)

def helloCallBack(id):
   tkMessageBox.showinfo( "Hello Python", "Presionaste el boton %s" % id)

def OnButtonClick(button_id):
    if button_id == 1:
        helloCallBack(1)
    elif button_id == 2:
        helloCallBack(2)

button2 = Button(ventana, text="2|SDA", command = lambda: OnButtonClick(1))
button2.grid(column=1, row=3, padx=(5,5), pady=(5,5))

raiz.mainloop()
