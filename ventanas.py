#Crea la ventana
class Ventana(object):
	def w():
		raiz = Tk()

		#Modifica la ventana y lo que hay dentro
		raiz.title('Sha1 Generator')
		raiz.geometry('300x250')

		    #Ventana
		ventana = Frame(raiz)
		ventana.grid(column=0, row=0, padx=(10,50), pady=(10,10))
		ventana.columnconfigure(0,weight=1)
		ventana.rowconfigure(0,weight=1)

		    #Etiquetas de texto
		tag = Label(ventana, text="Texto a encriptar")
		tag.grid(column=2, row=1, pady=(5,5))

		    #Botones
		button = Button(ventana, text="Hash it!", command=hacer_click)
		button.grid(column=2, row=3, padx=(5,5), pady=(5,5))

		    #Campo de entrada de texto
		entrada_txt = Entry(ventana, width=20, textvariable="")
		entrada_txt.grid(column=2, row=2)

		#Poner en marcha el ciclo de eventos
		raiz.mainloop()