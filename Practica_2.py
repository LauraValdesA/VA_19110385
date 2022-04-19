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

#while True:
#if kb.read_key()=='L':
 #   suma=res_izq+res_der
  #  resp = cv2.resize(suma, dsize=(300,500), interpolation = cv2.INTER_LINEAR)
   # cv2.imshow('suma',resp)
#break
contador=0
while True:
    if keyboard.read_key()=="v":
        cv2.waitKey(500)
        contador =contador+1
        print(contador)
        if contador==1:
            suma=res_izq+res_der
            resp = cv2.resize(suma, dsize=(300,500), interpolation = cv2.INTER_LINEAR)#resp1 = cv2.resize(resta, dsize=(300,500), interpolation = cv2.INTER_LINEAR)
            cv2.imshow('suma',resp)
            #break
        #cv2.imshow('suma',resp1)
        #cv2.waitKey(5000)
        #cv2.destroyWindow('suma')
        if contador==2:
            #cv2.destroyWindow('suma')
            resta=res_izq-res_der
            resp1 = cv2.resize(resta, dsize=(300,500), interpolation = cv2.INTER_LINEAR)
            cv2.imshow('resta',resp1)
            #break
        if contador==3:
            multi=res_izq*res_der
            resp2 = cv2.resize(multi, dsize=(300,500), interpolation = cv2.INTER_LINEAR)#resp1 = cv2.resize(resta, dsize=(300,500), interpolation = cv2.INTER_LINEAR)
            cv2.imshow('multiplicacion',resp2)
        if contador==4:
            div=res_der/res_izq
            resp3 = cv2.resize(div, dsize=(300,500), interpolation = cv2.INTER_LINEAR)#resp1 = cv2.resize(resta, dsize=(300,500), interpolation = cv2.INTER_LINEAR)
            cv2.imshow('division',resp3)
        if contador==5:
            arr = 255 / np.log(1 + np.max(res_izq))
            resp4 = arr * (np.log(res_izq + 1))
            resp4 = np.array(resp4, dtype = np.uint8)
            resp4 = cv2.resize(resp4, dsize=(300,500), interpolation = cv2.INTER_LINEAR)#resp1 = cv2.resize(resta, dsize=(300,500), interpolation = cv2.INTER_LINEAR)
            cv2.imshow('logaritmo',resp4)
        if contador==6:
            raiz=res_der** -res_izq
            resp5 = cv2.resize(raiz, dsize=(300,500), interpolation = cv2.INTER_LINEAR)#resp1 = cv2.resize(resta, dsize=(300,500), interpolation = cv2.INTER_LINEAR)
            cv2.imshow('Raiz',resp5)
        if contador==7:
            deriv=cv2.Laplacian(resp4,cv2.CV_64F)
            cv2.imshow('Derivada',deriv)
        if contador==8:
            potencia=res_der**res_izq
            resp6 = cv2.resize(potencia, dsize=(300,500), interpolation = cv2.INTER_LINEAR)#resp1 = cv2.resize(resta, dsize=(300,500), interpolation = cv2.INTER_LINEAR)
            cv2.imshow('Potencia',resp6)
        if contador==9:
            conjuncion= cv2.bitwise_and(res_der,res_izq)
            resp7 = cv2.resize(conjuncion, dsize=(300,500), interpolation = cv2.INTER_LINEAR)#resp1 = cv2.resize(resta, dsize=(300,500), interpolation = cv2.INTER_LINEAR)
            cv2.imshow('Conjuncion',resp7)
        if contador==10:
            disyuncion=cv2.bitwise_or(res_der,res_izq)
            cv2.imshow('Disyuncion',disyuncion)
        if contador==11:
            negacion=cv2.bitwise_not(res_der,res_izq)
            cv2.imshow('Negacion',negacion)
        if contador==12:
            M = np.float32([[1,0,100],[0,1,150]])
            traslacion = cv2.warpAffine(res_der,M,(res_der.shape[1],res_der.shape[0]))
            cv2.imshow('Traslacion',traslacion)
        if contador==13:
            escalado=cv2.resize(res_izq,(900,500))
            cv2.imshow('Escalado',escalado)
        if contador==14:
            M = cv2.getRotationMatrix2D((res_izq.shape[1]//2,res_izq.shape[0]//2),15,1)
            rotacion = cv2.warpAffine(res_izq,M,(res_izq.shape[1],res_izq.shape[0]))
            cv2.imshow('Rotacion',rotacion)
        if contador==15:
            filas,columnas = res_der.shape[:2]
            pts1 = np.float32([[50,50],[200,50],[50,200]])
            pts2 = np.float32([[10,100],[200,50],[100,250]])
            M = cv2.getAffineTransform(pts1,pts2)
            afin = cv2.warpAffine(res_der,M,(filas,columnas))
            cv2.imshow('A fin',afin)
        if contador==16:
            trans=cv2.transpose(res_der)
            cv2.imshow('Transpuesta',trans)
        if contador==17:
            break;
        
cv2.waitKey(5000)
cv2.destroyAllWindows()
