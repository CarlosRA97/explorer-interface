#!/usr/bin/env python

import cv2
import numpy as np
ix,iy=0,0
# mouse callback function
def cuadratica(x):
    return (x**2 + x + 1)/3
def mouse(event,x,y,flags,param):

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),50,(255,0,0),-1)
#Este bloque muestra las componentes x e y de los pixeles de la ventana corespondientes al raton
    elif event == cv2.EVENT_MOUSEMOVE:
        ix,iy = x,y
        p(ix,iy)
        print 'soy x(%i) y(%i)  estoy funcionando' % (ix,iy)
        return ix,iy

def p(ix,iy):
    cv2.circle(img,(ix,iy),10,(255,0,0),-1)

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',mouse)



while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
 #Nox
