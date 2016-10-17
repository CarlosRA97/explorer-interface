"""
Este es el programa final de lectro de linias pero no consigo limpiar lo suficiente la linia para poderleer con esactitu los pixeles
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

cam = cv2.VideoCapture(1)


print cam.get(3)

def dis():
    num = masc
    xy_val = np.nonzero(num)
    xy_val = np.array([np.nonzero(xy_val)])
    xy_val = np.transpose(np.nonzero(xy_val))
    print xy_val



while(1):
    rvel, frame= cam.read()


    #caps

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    rojo_max = np.array([255,196,255])
    rojo_min = np.array([0,0,54])
    masc = cv2.inRange(hsv, rojo_min, rojo_max)
    edges = cv2.Canny(frame, 100, 200)
    kernel = np.ones((6, 6), np.uint8)
    transformacion = cv2.morphologyEx(edges, cv2.MOTION_HOMOGRAPHY, kernel)
    sobelx8u = cv2.Sobel(frame, cv2.CV_8U, 1, 0, ksize=5)



    cv2.imshow('cam', frame)
    cv2.imshow('masc', masc)
    cv2.imshow('Edge', edges)
    cv2.imshow('filtrado', transformacion)
    cv2.imshow('sobelx8u', sobelx8u)

    #dis()

    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break
cv2.destroyAllWindows()

