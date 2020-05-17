
#Created on Thu May 14 08:59:52 2020

#@author: JULIAN LAMPREA

# tracking Object with OPENCV
import cv2 
import sys

print("version opencv",cv2.__version__)
print ("Version Python:",sys.version) 
captura= cv2.VideoCapture() # del laptop con 0 y 1 con webcam externa
#tracker= cv2.TrackerMOSSE_create() # mas rapido 38fps
captura.open(0)
captura.set(3, 640) # tamaño de la imagen
captura.set(4, 480)# tamaño de la imagen
tracker = cv2.TrackerCSRT_create() # mas lento # 18fps pero mas preciso
success,imagen= captura.read()# captura la primera imagen para seleccionar el objeto
cuadro = cv2.selectROI("Seguimiento", imagen,False) # espera que se selecciones el cuadro con el mouse
tracker.init(imagen,cuadro)

def pintarbox(imagen,cuadro):
    x,y,w,h = int(cuadro[0]), int(cuadro[1]),int(cuadro[2]),int(cuadro[3])
    cv2.rectangle(imagen, (x,y),((x+w),(y+h)), (255,0,0),3,1)
    cv2.putText(imagen, "Tracking",(75,75),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,255),2)
# Se desisnstalo opencv 4.1.2 con uninstall en el promp de anaconda
# se volvio a instalar con pip install opencv_contrib_python, se instalo opencv 4.2.0
while True:
    timer= cv2.getTickCount()
    success, imagen = captura.read()
    success,cuadro = tracker.update(imagen)
    if success:
        pintarbox(imagen,cuadro)
    else:
        cv2.putText(imagen, "sin objeto",(75,75),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),2)
    
    fps= cv2.getTickFrequency()/(cv2.getTickCount()-timer) # calculo fps 
    cv2.putText(imagen, str(int(fps)),(75,50),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),2)
    cv2.imshow("imagen camara", imagen)
    
    if cv2.waitKey(1) & 0xff == ord("q"):
        cv2.destroyAllWindows()# evita el error de show ventanas
        captura.release() # apaga la camara
        break
    
cv2.destroyAllWindows()
captura.release()
