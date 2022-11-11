import tkinter 
from tkinter import PhotoImage
from PIL import Image,ImageTk

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

#----------------------- Funciones ----------------------
def funcionOperacion():
    print("Me presionaste")

def abrirVentanaSuma():
    ventana.withdraw()
    win = tkinter.Tk()
    win.title("Proyecto Number")
    win.geometry("800x500")
    win.resizable(0,0)
    win.config(bg="blue violet")

#---------------------- Declaraciones -------------------
r = sr.Recognizer()

#----------------------- Ventana ------------------------
ventana = tkinter.Tk()
ventana.title("Proyecto Number")
ventana.geometry("800x500")
ventana.resizable(0,0)
ventana.config(bg="blue violet")

#----------------------- Imagenes ------------------------
#SUMA
imgSuma = Image.open('ProyectoNumber/suma.jpeg')
imgSuma = imgSuma.resize((100, 100), Image.ANTIALIAS) # Redimension (Alto, Ancho)
imgSuma = ImageTk.PhotoImage(imgSuma)
#RESTA
imgResta = Image.open('ProyectoNumber/resta.jpeg')
imgResta = imgResta.resize((100, 100), Image.ANTIALIAS) # Redimension (Alto, Ancho)
imgResta = ImageTk.PhotoImage(imgResta)
#MULTIPLICACION
imgMulti = Image.open('ProyectoNumber/multi.jpeg')
imgMulti = imgMulti.resize((100, 100), Image.ANTIALIAS) # Redimension (Alto, Ancho)
imgMulti = ImageTk.PhotoImage(imgMulti)
#DIVICION
imgDiv = Image.open('ProyectoNumber/div.jpeg')
imgDiv = imgDiv.resize((100, 100), Image.ANTIALIAS) # Redimension (Alto, Ancho)
imgDiv = ImageTk.PhotoImage(imgDiv)
#SALIR
imgSalir = Image.open('ProyectoNumber/salir.jpeg')
imgSalir = imgSalir.resize((90, 90), Image.ANTIALIAS) # Redimension (Alto, Ancho)
imgSalir = ImageTk.PhotoImage(imgSalir)

#----------------------- Etiqueta ------------------------
c1 = tkinter.Label(ventana, text= " Bienvenido ", bg="blue violet", font="Helvetica 30 bold")
c1.place(x=250, y=10,width=300,height=100 )

c2 = tkinter.Label(ventana, text= " ¿Qué acción quieres realizar? ", bg="blue violet", font="Helvetica 20 bold")
c2.place(x=150, y=100,width=500,height=25 )

bS = tkinter.Button(ventana, image=imgSuma, fg = "black",bg ="green", command= abrirVentanaSuma)
bS.place(x=100, y=200,width=100,height=100 )

bR = tkinter.Button(ventana, image=imgResta, fg = "black",bg ="green", command= funcionOperacion)
bR.place(x=270, y=200,width=100,height=100 )

bM = tkinter.Button(ventana, image=imgMulti, fg = "black",bg ="green", command= funcionOperacion)
bM.place(x=435, y=200,width=100,height=100 )

bD = tkinter.Button(ventana, image=imgDiv, fg = "black",bg ="green", command= funcionOperacion)
bD.place(x=600, y=200,width=100,height=100 )

salir = tkinter.Button(ventana, image=imgSalir)
salir.place(x=355, y=350,width=90,height=90 )



ventana.mainloop()

tts = gTTS('Bienvenido', lang='es-us')
tts.save('bienvenido.mp3')
playsound('bienvenido.mp3')

tts = gTTS('¿Qué acción quieres realizar?', lang='es-us')
tts.save('accion.mp3')
playsound('accion.mp3')

