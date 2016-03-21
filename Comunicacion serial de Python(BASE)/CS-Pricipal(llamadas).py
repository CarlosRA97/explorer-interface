from Movimientos import *
import sys

movimientos = Movimiento()
while 1:
    tecla = sys.stdin.read(1)
    if tecla =='w':
        movimientos.avance()
    print 'Has presionado ', tecla
