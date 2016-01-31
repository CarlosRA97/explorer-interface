#!/usr/bin/env python

'''
para salir del programa pulsa "q"
'''
#impotamao los modulos necesarios
import cv2
import numpy as np
# creamos un opjento con el nombre de cap el cual sera el que seconecte a la camara
# definimos la camara
cap = cv2.VideoCapture(1)
#esperamos a que la camara este trasmitiendo
while True:
    ret, frame = cap.read() # rent?="refrecar" creamos un opjeto "frame" con las imajenes de la camara
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #la umajen en color BGR(azul berde rojo) se pasan a escala de grises

    cv2.imshow('fame', frame)#mostramos las imajenes en una ventana de titulo "fame"
    cv2.imshow('gris', gris) #muestra la imajen en gris "..."
    #creamos un condicionalpra cerrar la ventana al presionar la q con un ciclo de espera
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release() #mostramos
cv2.destroyAllWindows()#cerramos
