import tkinter 
from tkinter import PhotoImage
from PIL import Image,ImageTk

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

import Manos as cff
import VRespuesta
import VRSuma as vs
import time as t

#---------------------- Declaraciones -------------------
r = sr.Recognizer()
ventana = tkinter.Tk()
#----------------------- Funciones ----------------------

def abrirVentanaSuma():
    
    ventana.withdraw()
    number1=cff.abrirCamara()
    print(str(number1))
    number2=cff.abrirCamara()
    print(str(number2))
    resultado = number1 + number2
    print(str(resultado))
    vs.abrirVentanaSumaR(number1, number2, resultado)
    
    
def abrirVentanaResta():
    ventana.withdraw()
    number1=cff.abrirCamara()
    print(str(number1))
    number2=cff.abrirCamara()
    print(str(number2))
    resultado = number1 - number2
    print(str(resultado))
    VRespuesta.abrirVentanaRestaR(number1, number2, resultado)

    

def abrirVentanaMul():
    ventana.withdraw()
    number1=cff.abrirCamara()
    print(str(number1))
    number2=cff.abrirCamara()
    print(str(number2))
    resultado = number1 * number2
    print(str(resultado))
    VRespuesta.abrirVentanaMulR(number1, number2, resultado)

    

def abrirVentanaDiv():
    ventana.withdraw()
    number1=cff.abrirCamara()
    print(str(number1))
    number2=cff.abrirCamara()
    print(str(number2))
    if number2 == 0 :
        resultado = 0
    else:
        resultado = number1 / number2
    print(str(resultado))
    VRespuesta.abrirVentanaDivR(number1, number2, resultado)
   

def ventanaPrincipal():
#----------------------- Ventana ------------------------
    #ventana = tkinter.Tk()
    ventana.title("Proyecto Number")
    ventana.geometry("800x500")
    ventana.resizable(0,0)
    ventana.config(bg="blue violet")

#----------------------- Imagenes ------------------------
    dir = 'C:/Users/Alex/Desktop/PROYECTO-V4/Proyecto-InterfacesUsuario/ProyectoNumber/image' 
#SUMA
    imgSuma = Image.open(dir+'/suma.jpeg')
    imgSuma = imgSuma.resize((100, 100), Image.ANTIALIAS) # Redimension (Alto, Ancho)
    imgSuma = ImageTk.PhotoImage(imgSuma)
#RESTA
    imgResta = Image.open(dir+'/resta.jpeg')
    imgResta = imgResta.resize((100, 100), Image.ANTIALIAS) # Redimension (Alto, Ancho)
    imgResta = ImageTk.PhotoImage(imgResta)
#MULTIPLICACION
    imgMulti = Image.open(dir+'/multi.jpeg')
    imgMulti = imgMulti.resize((100, 100), Image.ANTIALIAS) # Redimension (Alto, Ancho)
    imgMulti = ImageTk.PhotoImage(imgMulti)
#DIVISION
    imgDiv = Image.open(dir+'/div.jpeg')
    imgDiv = imgDiv.resize((100, 100), Image.ANTIALIAS) # Redimension (Alto, Ancho)
    imgDiv = ImageTk.PhotoImage(imgDiv)
#SALIR
    imgSalir = Image.open(dir+'/exit.png')
    imgSalir = imgSalir.resize((90, 90), Image.ANTIALIAS) # Redimension (Alto, Ancho)
    imgSalir = ImageTk.PhotoImage(imgSalir)

#----------------------- Etiqueta ------------------------
    c1 = tkinter.Label(ventana, text= " Bienvenido ", bg="blue violet", font="Helvetica 30 bold")
    c1.place(x=250, y=10,width=300,height=100 )

    c2 = tkinter.Label(ventana, text= " ¿Qué acción quieres realizar? ", bg="blue violet", font="Helvetica 20 bold")
    c2.place(x=150, y=100,width=500,height=25 )

    bS = tkinter.Button(ventana, image=imgSuma, bg='blue violet', fg='blue violet', command= abrirVentanaSuma)
    bS.place(x=100, y=200,width=100,height=100 )

    bR = tkinter.Button(ventana, image=imgResta, bg='blue violet', fg='blue violet', command= abrirVentanaResta)
    bR.place(x=270, y=200,width=100,height=100 )

    bM = tkinter.Button(ventana, image=imgMulti, bg='blue violet', fg='blue violet', command= abrirVentanaMul)
    bM.place(x=435, y=200,width=100,height=100 )

    bD = tkinter.Button(ventana, image=imgDiv, bg='blue violet', fg='blue violet', command= abrirVentanaDiv)
    bD.place(x=600, y=200,width=100,height=100 )

    salir = tkinter.Button(ventana, image=imgSalir, bg='blue violet', fg='blue violet', command=exit)
    salir.place(x=355, y=350,width=90,height=90 )

    ventana.mainloop()



#----------------- LLama a la ventana principal ----------------
ventanaPrincipal()

tts = gTTS('Bienvenido', lang='es-us')
tts.save('bienvenido.mp3')
playsound('bienvenido.mp3')

tts = gTTS('¿Qué acción quieres realizar?', lang='es-us')
tts.save('accion.mp3')
playsound('accion.mp3')

