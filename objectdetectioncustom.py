# -*- coding: utf-8 -*-
"""
Created on Fri May 15 18:14:41 2020

@author: JULIAN LAMPREA
"""

import cv2

################################################################
path = 'Halcon/classifier/cascade.xml'  # PATH OF THE CASCADE/ srranca desde donde se guarda el .py
cameraNo = 0                       # CAMERA NUMBER
objectName = 'H.Millenario'       # OBJECT NAME TO DISPLAY
frameWidth= 640                     # DISPLAY WIDTH
frameHeight = 480                  # DISPLAY HEIGHT
color= (255,0,255)
#################################################################

# hace la ventana de video de 640 x 480
# se cambia a formato CAP_DSHOW para activar la webcam 0, 1 laptop. MSMF no funciona
cap = cv2.VideoCapture(cameraNo,cv2.CAP_DSHOW)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

def empty(a):
    pass

# CREATE TRACKBAR
cv2.namedWindow("Result")
cv2.resizeWindow("Result",frameWidth,frameHeight+100)
cv2.createTrackbar("Scale","Result",400,1000,empty)
cv2.createTrackbar("Neig","Result",8,50,empty)
cv2.createTrackbar("Min Area","Result",0,100000,empty)
cv2.createTrackbar("Brightness","Result",180,255,empty)

# LOAD THE CLASSIFIERS DOWNLOADED
cascade = cv2.CascadeClassifier(path)

while True:
    # SET CAMERA BRIGHTNESS FROM TRACKBAR VALUE
    cameraBrightness = cv2.getTrackbarPos("Brightness", "Result")
    cap.set(10, cameraBrightness)
    # GET CAMERA IMAGE AND CONVERT TO GRAYSCALE
    success, img = cap.read()
    if success:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # DETECT THE OBJECT USING THE CASCADE
        scaleVal =1 + (cv2.getTrackbarPos("Scale", "Result") /1000)
        neig=cv2.getTrackbarPos("Neig", "Result")
        objects = cascade.detectMultiScale(gray,scaleVal, neig)
        # DISPLAY THE DETECTED OBJECTS
        for (x,y,w,h) in objects:
            area = w*h
            minArea = cv2.getTrackbarPos("Min Area", "Result")
            if area >minArea:
                cv2.rectangle(img,(x,y),(x+w,y+h),color,3)
                cv2.putText(img,objectName,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
                roi_color = img[y:y+h, x:x+w]

        cv2.imshow("Result", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cv2.destroyAllWindows()
cap.release()        
        