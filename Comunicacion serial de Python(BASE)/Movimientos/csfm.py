import serial

Ser = serial.Serial('COM3', 38400, timeout=1)
if Ser.is_open == True:
    Ser.close()
    pass

class Movimiento():
    def __init__(self, velocidad):
        self.velocidad = velocidad

    def avance(self):
        Ser.open()
        Ser.write('a')
        Ser.close()

    def retrocder(self):
        pass



if __name__ == '__main__':
    op = Movimiento()
