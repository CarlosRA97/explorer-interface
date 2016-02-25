import cv2
import numpy as np
import sys

sys.settrace


cap = cv2.VideoCapture(0)
def detecting_pixels(event,x,y,flags,param):
    # if event == cv2.EVENT_MOUSEMOVE:
    #     print 'Coordenada X= (%i) Y= (%i)' % (x,y)
    if event == cv2.EVENT_LBUTTONDOWN:
        # analisisPix(x,y)
        print 'Pixele selecionado (%i, %i)' % (x,y)

#def analisisPix(ix,iy):
    #px = frame[ix,iy]

while(1):

#Bolque 1: captura y tratamiento de la camara
    #Take each frame
    _, frame = cap.read()

    #Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#Bloque 2: variables de color
    lower_blue = np.array([0,51,25])

    upper_blue = np.array([153,255,153])

#Bloque 3:Creacion de mascaras
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
#Bloque 4: muestra de las mascaras

    #cv2.imshow('mask',mask)
    #cv2.imshow('res',res)
    #cv2.namedWindow('frame')
    cv2.setMouseCallback('frame',detecting_pixels)
    cv2.imshow('frame', frame)
#Bloque 5: control de fin de programa
    k = cv2.waitKey(5) & 0xFF
    if k == ord('k'):
        break

cv2.destroyAllWindows()
