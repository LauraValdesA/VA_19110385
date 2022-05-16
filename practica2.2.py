import numpy as np
from matplotlib import pyplot as plt
import cv2 #opencv
import matplotlib.image as img
import keyboard 


#plantilla=Tk()
#plant=Frame(plantilla)
#plantilla.title("Practica 2")
#plantilla.geometry("1500x900")

#imagen=PhotoImage(file="practica2_i1.png")
#fondo=Label(plant,image=imagen).place(x=100, y=100)
#plantilla.mainloop

imagen1=cv2.imread('imagenes/practica2_i1.png',1)
res1=cv2.resize(imagen1, dsize=(300,500), interpolation = cv2.INTER_LINEAR)
cv2.imshow('imagen1', res1)

imagen2=cv2.imread('imagenes/practica2_i2.png',1)
res2=cv2.resize(imagen2, dsize=(300,500), interpolation = cv2.INTER_LINEAR)
cv2.imshow('imagen2', res2)

izq=cv2.imread('imagenes/practica2_i1.png',1)
res_izq=cv2.resize(izq, dsize=(300,500))
der=cv2.imread('imagenes/practica2_i2.png',1)
res_der=cv2.resize(der, dsize=(300,500))

suma=res_izq+res_der
cv2.imshow('suma',suma)
cv2.waitKey('109')
cv2.destroyAllWindows()

resta=res_izq-res_der
cv2.imshow('resta',resta)
cv2.waitKey(0)
cv2.destroyAllWindows()
