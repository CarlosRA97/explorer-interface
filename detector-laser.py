"""
Este progarama se divide en dos funciones 'parametros' => se encarga de extraer y mostrar el anco y el largo
de la imajen: y 'raton' => que se encarga de extraer el comos del pixel con la situacion del raton

"""

import cv2
import numpy as np


# Imagen

img = cv2.imread('Linea laser tst2.jpg')

# Mascaras

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
rojo_max = np.array([254, 255, 255])
rojo_min = np.array([0, 0, 230])
masc = cv2.inRange(hsv, rojo_min, rojo_max)
color = cv2.bitwise_and(img, img, mask=masc)


def imageSize():
    datos = img.shape
    dimensiones = datos[1], datos[0]
    print 'Parametro: ', dimensiones
    return dimensiones


def mousePosWhenClick(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:    #comprueba si el evento llamado es del clik
        print img[x, y]                    #imprime el balor del pixel
        print flags
        print param

        
# Ventana

def main():
    cv2.imshow('img', img)
    cv2.imshow('hsv', hsv)
    cv2.imshow('masc', masc)
    cv2.setMouseCallback('hsv', mousePosWhenClick)
    cv2.imshow('color', color)


main()
cv2.waitKey(0)
#cv2.imwrite('Img_hsv.png',hsv)  #cre auna img estraida de la capa hsv
cv2.destroyAllWindows()
