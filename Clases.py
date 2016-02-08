#!/usr/bin/env python

class Auto(object):
	condicion = "nuevo"
	def __init__(self, modelo, color, kpl):
		self.modelo = modelo
		self.color = color
		self.kpl = kpl
    
	def verAuto(self):
	    return "Este es un %s color %s que alcanza %s kpl." % (self.modelo,self.color,str(self.kpl))
	    
	def manejarAuto(self):
	    self.condicion = "usado"


class AutoElectrico(Auto):
    def __init__(self,tipoDeBateria,modelo, color, kpl):
        self.modelo = modelo
        self.color = color
        self.kpl = kpl
        self.tipoDeBateria = tipoDeBateria
      
    def manejarAuto(self):
	    self.condicion = "como nuevo"




miAuto = AutoElectrico("sales fundidas","Clio", "gris", 16)

print miAuto.condicion
miAuto.manejarAuto()
print miAuto.condicion

print miAuto.tipoDeBateria

