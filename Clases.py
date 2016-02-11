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




# miAuto = AutoElectrico("sales fundidas","Clio", "gris", 16)
#
# print miAuto.condicion
# miAuto.manejarAuto()
# print miAuto.condicion
#
# print miAuto.tipoDeBateria



class Customer(object):
    """A customer of ABC Bank with a checking account. Customers have the
    following properties:

    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """

    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        return self.balance


whois = raw_input("Quien eres?: ")
currency = "euros"


_ = Customer(whois)
print "Hola,",_.name

def sacar():
	take = input("Cuanto quiere sacar?: ")
	if take != "":
		_.withdraw(take)
		print "Has retirado %d %s de tu cuenta, saldo actual %d %s" % (take,currency,_.balance,currency)
	else:
		print "Escribe una cantidad"
		sacar()

while True:
	print "Tu saldo actual es de",_.balance,currency

	op = raw_input("Que operacion quiere realizar?: (sacar|meter)")

	if op == "meter":
		take = input("Cuanto quiere meter?: ")
		_.deposit(take)
		print "Has introducido",_.balance,currency

	elif op == "sacar":
		sacar()

	else:
		print "Hasta luego, %s!" % _.name
		break
