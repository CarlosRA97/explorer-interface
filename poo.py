class Humano(object):
	def __init__(self,edad):
		self.edad = edad
		print "Soy un nuevo objeto"

	def hablar(self,mensaje):
		print mensaje

class IngSistemas(Humano):
	def programar(self,lenguaje):
		print "Voy a programar en", lenguaje

class LicDerecho(Humano):
	def __init__(self,escuela):
		print "Licenciado en Derecho ingresado de:", escuela

	def estudiarCaso(self,de):
		print "Debo estudiar el caso de", de
		
class estudioso(IngSistemas,LicDerecho):
	pass
		
pepe = estudioso("UMA")

pepe.hablar("Hola soy de herencia multiple")

pepe.programar("C++")

pepe.estudiarCaso("Pedro")