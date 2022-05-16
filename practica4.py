import cv2
import numpy as np

img=np.zeros((500,800,3),np.uint8)

img=cv2.rectangle(img, (190,40), (610,460), (255,0,0), 5)

img=cv2.ellipse(img, (305,355), (160,10), 138, 0,360, (0,69,255), 3)
img=cv2.ellipse(img, (505,155), (160,10), 132, 0,360, (0,69,255), 3)
img=cv2.ellipse(img, (305,155), (165,10), 45, 0,360, (0,69,255), 3)
img=cv2.ellipse(img, (500,350), (160,10), 45, 0,360, (0,69,255), 3)



img=cv2.circle(img, (400,250), 200, (199,21,133),5)

pts=np.array([[400,60],[590,250],[400,440],[210,250]],np.int32)
pts=pts.reshape((-1,1,2))
cv2.polylines(img,[pts], True, (255,192,203),5)

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Melissa', (10,30), font, 1, (216,191,216),2)

frac=img[30:340, 410:630]

cv2.imshow('imagen1', img)
cv2.imshow('imagen2', frac)

cv2.waitKey(0)
cv2.destroyAllWindows()
