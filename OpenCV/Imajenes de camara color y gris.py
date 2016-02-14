#!/usr/bin/env python

'''
para salir del programa pulsa "q"
'''
#importamos los modulos necesarios
import cv2
import numpy as np
# creamos un objeto con el nombre de cap el cual sera el que se conecte a la camara
# definimos la camara
cap = cv2.VideoCapture(1)
#esperamos a que la camara este trasmitiendo
while True:
    ret, frame = cap.read() # rent?="refrecar" creamos un objeto "frame" con las imagenes de la camara
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #la imajen en color BGR(azul, verde, rojo) se pasan a escala de grises

    cv2.imshow('fame', frame) # mostramos las imajenes en una ventana de titulo "fame"
    cv2.imshow('gris', gris)  # muestra la imajen en gris "..."
    # creamos un condicional para cerrar la ventana al presionar la q con un ciclo de espera
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print __doc__
cap.release() #mostramos
cv2.destroyAllWindows()#cerramos
