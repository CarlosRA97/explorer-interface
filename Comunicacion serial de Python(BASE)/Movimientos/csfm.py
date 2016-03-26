import serial
import threading


class Movimiento():
	def __init__(self, velocidad):
		self.ser = serial.Serial('COM3', 38400, timeout=1)
		self.velocidad = velocidad
		if self.ser.is_open:
			self.ser.close()

	def avance(self):
		self.ser.open()
		self.ser.write('a')
		self.ser.close()

	# TODO: Establecer los movimientos mediante serial
	
	def retroceder(self):
		pass

	def girar_derecha(self, grados):
		pass

	def girar_izquierda(self, grados):
		pass


if __name__ == '__main__':
	op = Movimiento()
