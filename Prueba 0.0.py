from tkinter import *
raiz = Tk()
 
raiz.title('Hola mundo')
raiz.geometry('300x400')

 name = "" # nobre de la variable
 
# propiedades de la ventana

ventana = Frame(raiz)
ventana.grid(column=0, row=0, padx=(10,50), pady=(10,10)) #posicion y anchura anchura
ventana.columnconfigure(0,weight=1)# centrado de la bentana
ventana.rowconfigure(0,weight=1)

# etiquetas

tag = Label(ventana, text="Nombre")
tag.grid(column=1, row=1, padx=(5,5), pady=(5,5))

# entradas de texto

entrada_nombre = Entry(ventana, width=20, textvariable=name)
entrada_nombre.grid(column=2, row=1)

# escribir variable

tag = Label(ventana, text= name)
tag.grid(column=1, row=2, padx=(5,5), pady=(5,5))

raiz.mainloop()
