import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    _, frame=cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #azul
    #color_bajo = np.array([100,0,50])
    #color_alto = np.array([255,255,200])

    #rojo
    #color_bajo = np.array([50,0,0])
    #color_alto = np.array([200,255,255])

    #verde
    #color_bajo = np.array([30,50,10])
    #color_alto = np.array([250,200,255])

    #rosa
    #color_bajo = np.array([100,100,0])
    #color_alto = np.array([200,255,255])

    color_bajo = np.array([10,100,0])
    color_alto = np.array([250,200,255])

    mask = cv2.inRange(hsv, color_bajo, color_alto)

    res=cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    k=cv2.waitKey(5) & 0xFF
    if k==27:
        break

cv2.destroyAllWindows()
cap.release()
