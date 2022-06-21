import matplotlib.pyplot as plt
import pylab
import cv2
import numpy as np

#Imagen 
imagen = plt.imread ("imagenes/Practica10_img.jpg")
imagen2=cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB)

#Kernel
enfoque=np.ones((5,5), np.float32)/30

emboss=np.array([[-2, -1, 0],
                 [-1, 1, 1],
                 [0, 1, 2]])
                  
bordes = np.array([[-1, -1, -1],
                    [-1, 8, -1],
                    [-1, -1, -1]])                                                     

conv_enf = cv2.filter2D(imagen, -1, enfoque) 
conv_med = cv2.filter2D(conv_enf, -1, emboss)
conv_bor = cv2.filter2D(imagen, -1, bordes) 


plt.subplot(2,2,1)
plt.imshow (imagen)
plt.title('Imagen Original')
plt.axis('off')
 
plt.subplot(2,2,2)
plt.imshow (conv_enf)
plt.title('Enfoque')
plt.axis('off')

plt.subplot(2,2,3)
plt.imshow (conv_med)
plt.title('Emboss')
plt.axis('off')

plt.subplot(2,2,4)
plt.imshow (conv_bor)
plt.title('Filtro')
plt.axis('off') 

pylab.show()
