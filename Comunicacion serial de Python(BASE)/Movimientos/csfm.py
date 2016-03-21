import serial
import threading


class Movimiento():
	def __init__(self):
		self.ser = serial.Serial('COM3', 38400, timeout=1)
		self.velocidad = velo
		if self.ser.is_open:
			self.ser.close()

	def avance(self):
		self.ser.open()
		self.ser.write('a')
		self.ser.close()

	def retroceder(self, velocidad):
		pass

	def girar_derecha(self, velocidad, grados):
		pass

	def girar_izquierda(self, velocidad, grados):
		pass


if __name__ == '__main__':
	op = Movimiento(
