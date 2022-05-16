import cv2
import numpy as np

img = cv2.imread('imagenes/practica_9_original1.jpg')
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template = cv2.imread('imagenes/practica_9_patron2.jpg',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img2,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.75
loc = np.where( res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

cv2.imshow('Detected',img)
