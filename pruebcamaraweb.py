# -*- coding: utf-8 -*-
"""
Created on Thu May 14 19:18:42 2020

@author: JULIAN LAMPREA
"""
import cv2 

cv2.destroyAllWindows()
captura = cv2.VideoCapture(0).release()
captura= cv2.VideoCapture(1).release()
# se debe cambiar al formato para la webcam a CAP_DSHOW, MSMF no sirve.
captura = cv2.VideoCapture(0,cv2.CAP_DSHOW) # del laptop con 1 y 0 con webcam externa


#captura.set(3, 480) # tamaño de la imagen
#captura.set(4, 640)# tamaño de la imagen


while True:
    timer= cv2.getTickCount()
    success, imagen = captura.read()
    # se confirma que se cree una imagen para que espere la ventana
    if success:
        fps= cv2.getTickFrequency()/(cv2.getTickCount()-timer) # calculo fps 
        cv2.putText(imagen, str(int(fps)),(75,50),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),2)
        cv2.imshow("imagen camara", imagen)
        
        if cv2.waitKey(1) & 0xff == ord("q"):
            cv2.destroyAllWindows()# evita el error de show ventanas
            captura.release() # apaga la camara
            break
    
cv2.destroyAllWindows()
captura.release()