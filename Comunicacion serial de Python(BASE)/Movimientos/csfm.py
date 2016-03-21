import serial

Ser = serial.Serial('COM3', 38400, timeout=1)
if Ser.is_open == True:
    Ser.close()
    pass

class Movimiento():
    def __init__(self):
        print('Movimiento funciona')

    def avance(self):
        Ser.open()
        Ser.write('a')
        Ser.close()


if __name__ == '__main__':
    op = Movimiento()
