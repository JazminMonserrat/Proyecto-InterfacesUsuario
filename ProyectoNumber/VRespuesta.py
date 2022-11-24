import tkinter 
from tkinter import PhotoImage
from PIL import Image,ImageTk

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

#---------------------- Declaraciones -------------------
r = sr.Recognizer()

def abrirVentanaSumaR(n1, n2, r):

    #import Ventana as v
    vResultado = tkinter.Tk()
    vResultado.title("Resultado")
    vResultado.geometry("800x500")
    vResultado.resizable(0,0)
    vResultado.config(bg="blue violet")

    #-----------------------IMAGENES------------------------

    dir = 'C:/Users/Alex/Desktop/PROYECTO-V4/Proyecto-InterfacesUsuario/ProyectoNumber/image'

    imgS = Image.open(dir+'/s.jpg')
    imgS = imgS.resize((50, 50), Image.ANTIALIAS) # Redimension (Alto, Ancho)
    imgS = ImageTk.PhotoImage(imgS)

    imgR = Image.open(dir+'/resultado.jpg')
    imgR = imgR.resize((50, 50), Image.ANTIALIAS) # Redimension (Alto, Ancho)
    imgR = ImageTk.PhotoImage(imgR)

    fondo = Image.open(dir+'/crayons.png')
    fondo = fondo.resize((160, 160), Image.ANTIALIAS) # Redimension (Alto, Ancho)
    fondo = ImageTk.PhotoImage(fondo)

#--------------------------- Etiqueta ---------------------------------
    c1 = tkinter.Label(vResultado, text= " RESULTADO ", bg="blue violet", font="Helvetica 30 bold")
    c1.place(x=155, y=10,width=500,height=100)

    operacion = tkinter.Label(vResultado, text= "-- SUMA -- ", bg="blue violet", font="Helvetica 15 bold")
    operacion.place(x=345, y=90,width=120,height=23)

    numero1 = tkinter.Label(vResultado, text=n1, bg="blue violet", font="Helvetica 47 bold")
    numero1.place(x=130, y=180,width=100,height=90 )

    numero2 = tkinter.Label(vResultado, text=n2, bg="blue violet", font="Helvetica 47 bold")
    numero2.place(x=320, y=180,width=100,height=90 )

    resultado = tkinter.Label(vResultado, text=r, bg="blue violet", font="Helvetica 47 bold")
    resultado.place(x=480, y=180,width=200,height=90 )

    cs = tkinter.Label(vResultado, image=imgS)
    cs.place(x=250, y=200,width=50,height=50 )

    cr = tkinter.Label(vResultado, image=imgR)
    cr.place(x=430, y=200,width=50,height=50 )

    #----------------------- Etiquetas de fondo ------------------------

    f1 = tkinter.Label(vResultado, image=fondo, bg='blue violet', fg='blue violet')
    f1.place(x=0, y=410,width=160,height=160 )

    f2 = tkinter.Label(vResultado, image=fondo, bg='blue violet', fg='blue violet')
    f2.place(x=164, y=410,width=160,height=160 )
    
    f3 = tkinter.Label(vResultado, image=fondo, bg='blue violet', fg='blue violet')
    f3.place(x=328, y=410,width=160,height=160 )

    f4 = tkinter.Label(vResultado, image=fondo, bg='blue violet', fg='blue violet')
    f4.place(x=492, y=410,width=160,height=160 )
    
    f5 = tkinter.Label(vResultado, image=fondo, bg='blue violet', fg='blue violet')
    f5.place(x=656, y=410,width=160,height=160 )

    vResultado.mainloop()
   














def abrirVentanaRestaR(n1, n2, r):

    vResultado = tkinter.Tk()
    vResultado.title("Resultado")
    vResultado.geometry("800x500")
    vResultado.resizable(0,0)
    vResultado.config(bg="blue violet")

    #-----------------------IMAGENES------------------------

    dir = 'C:/Users/Alex/Desktop/PROYECTO-V4/Proyecto-InterfacesUsuario/ProyectoNumber/image'

    imgS = Image.open(dir+'/r.jpg')
    imgS = imgS.resize((50, 50), Image.ANTIALIAS) # Redimension (Alto, Ancho)
    imgS = ImageTk.PhotoImage(imgS)

    imgR = Image.open(dir+'/resultado.jpg')
    imgR = imgR.resize((50, 50), Image.ANTIALIAS) # Redimension (Alto, Ancho)
    imgR = ImageTk.PhotoImage(imgR)

    fondo = Image.open(dir+'/crayons.png')
    fondo = fondo.resize((160, 160), Image.ANTIALIAS) # Redimension (Alto, Ancho)
    fondo = ImageTk.PhotoImage(fondo)

#--------------------------- Etiqueta ---------------------------------
    c1 = tkinter.Label(vResultado, text= " RESULTADO ", bg="blue violet", font="Helvetica 30 bold")
    c1.place(x=155, y=10,width=500,height=100)

    operacion = tkinter.Label(vResultado, text= "-- RESTA -- ", bg="blue violet", font="Helvetica 15 bold")
    operacion.place(x=345, y=90,width=120,height=23)

    numero1 = tkinter.Label(vResultado, text=n1, bg="blue violet", font="Helvetica 47 bold")
    numero1.place(x=130, y=180,width=100,height=90 )

    numero2 = tkinter.Label(vResultado, text=n2, bg="blue violet", font="Helvetica 47 bold")
    numero2.place(x=320, y=180,width=100,height=90 )

    resultado = tkinter.Label(vResultado, text=r, bg="blue violet", font="Helvetica 47 bold")
    resultado.place(x=480, y=180,width=200,height=90 )

    cs = tkinter.Label(vResultado, image=imgS)
    cs.place(x=250, y=200,width=50,height=50 )

    cr = tkinter.Label(vResultado, image=imgR)
    cr.place(x=430, y=200,width=50,height=50 )

    #----------------------- Etiquetas de fondo ------------------------

    f1 = tkinter.Label(vResultado, image=fondo, bg='blue violet', fg='blue violet')
    f1.place(x=0, y=410,width=160,height=160 )

    f2 = tkinter.Label(vResultado, image=fondo, bg='blue violet', fg='blue violet')
    f2.place(x=164, y=410,width=160,height=160 )
    
    f3 = tkinter.Label(vResultado, image=fondo, bg='blue violet', fg='blue violet')
    f3.place(x=328, y=410,width=160,height=160 )

    f4 = tkinter.Label(vResultado, image=fondo, bg='blue violet', fg='blue violet')
    f4.place(x=492, y=410,width=160,height=160 )
    
    f5 = tkinter.Label(vResultado, image=fondo, bg='blue violet', fg='blue violet')
    f5.place(x=656, y=410,width=160,height=160 )

    vResultado.mainloop()













def abrirVentanaMulR(n1, n2, r):

    vResultado = tkinter.Tk()
    vResultado.title("Resultado")
    vResultado.geometry("800x500")
    vResultado.resizable(0,0)
    vResultado.config(bg="blue violet")

    #-----------------------IMAGENES------------------------

    dir = 'C:/Users/Alex/Desktop/PROYECTO-V4/Proyecto-InterfacesUsuario/ProyectoNumber/image'

    imgS = Image.open(dir+'/m.jpg')
    imgS = imgS.resize((50, 50), Image.ANTIALIAS) # Redimension (Alto, Ancho)
    imgS = ImageTk.PhotoImage(imgS)

    imgR = Image.open(dir+'/resultado.jpg')
    imgR = imgR.resize((50, 50), Image.ANTIALIAS) # Redimension (Alto, Ancho)
    imgR = ImageTk.PhotoImage(imgR)

    fondo = Image.open(dir+'/crayons.png')
    fondo = fondo.resize((160, 160), Image.ANTIALIAS) # Redimension (Alto, Ancho)
    fondo = ImageTk.PhotoImage(fondo)

#--------------------------- Etiqueta ---------------------------------
    c1 = tkinter.Label(vResultado, text= " RESULTADO ", bg="blue violet", font="Helvetica 30 bold")
    c1.place(x=155, y=10,width=500,height=100)

    operacion = tkinter.Label(vResultado, text= "-- MULTIPLICACIÓN -- ", bg="blue violet", font="Helvetica 15 bold")
    operacion.place(x=295, y=90,width=220,height=23)

    numero1 = tkinter.Label(vResultado, text=n1, bg="blue violet", font="Helvetica 47 bold")
    numero1.place(x=130, y=180,width=100,height=90 )

    numero2 = tkinter.Label(vResultado, text=n2, bg="blue violet", font="Helvetica 47 bold")
    numero2.place(x=320, y=180,width=100,height=90 )

    resultado = tkinter.Label(vResultado, text=r, bg="blue violet", font="Helvetica 47 bold")
    resultado.place(x=480, y=180,width=200,height=90 )

    cs = tkinter.Label(vResultado, image=imgS)
    cs.place(x=250, y=200,width=50,height=50 )

    cr = tkinter.Label(vResultado, image=imgR)
    cr.place(x=430, y=200,width=50,height=50 )

    #----------------------- Etiquetas de fondo ------------------------

    f1 = tkinter.Label(vResultado, image=fondo, bg='blue violet', fg='blue violet')
    f1.place(x=0, y=410,width=160,height=160 )

    f2 = tkinter.Label(vResultado, image=fondo, bg='blue violet', fg='blue violet')
    f2.place(x=164, y=410,width=160,height=160 )
    
    f3 = tkinter.Label(vResultado, image=fondo, bg='blue violet', fg='blue violet')
    f3.place(x=328, y=410,width=160,height=160 )

    f4 = tkinter.Label(vResultado, image=fondo, bg='blue violet', fg='blue violet')
    f4.place(x=492, y=410,width=160,height=160 )
    
    f5 = tkinter.Label(vResultado, image=fondo, bg='blue violet', fg='blue violet')
    f5.place(x=656, y=410,width=160,height=160 )

    vResultado.mainloop()










def abrirVentanaDivR(n1, n2, r):

    vResultado = tkinter.Tk()
    vResultado.title("Resultado")
    vResultado.geometry("800x500")
    vResultado.resizable(0,0)
    vResultado.config(bg="blue violet")

    #-----------------------IMAGENES------------------------

    dir = 'C:/Users/Alex/Desktop/PROYECTO-V4/Proyecto-InterfacesUsuario/ProyectoNumber/image'

    imgS = Image.open(dir+'/d.jpg')
    imgS = imgS.resize((50, 50), Image.ANTIALIAS) # Redimension (Alto, Ancho)
    imgS = ImageTk.PhotoImage(imgS)

    imgR = Image.open(dir+'/resultado.jpg')
    imgR = imgR.resize((50, 50), Image.ANTIALIAS) # Redimension (Alto, Ancho)
    imgR = ImageTk.PhotoImage(imgR)

    fondo = Image.open(dir+'/crayons.png')
    fondo = fondo.resize((160, 160), Image.ANTIALIAS) # Redimension (Alto, Ancho)
    fondo = ImageTk.PhotoImage(fondo)

#--------------------------- Etiqueta ---------------------------------
    c1 = tkinter.Label(vResultado, text= " RESULTADO ", bg="blue violet", font="Helvetica 30 bold")
    c1.place(x=155, y=10,width=500,height=100)

    operacion = tkinter.Label(vResultado, text= "-- DIVISIÓN -- ", bg="blue violet", font="Helvetica 15 bold")
    operacion.place(x=290, y=90,width=220,height=23)

    numero1 = tkinter.Label(vResultado, text=n1, bg="blue violet", font="Helvetica 47 bold")
    numero1.place(x=130, y=180,width=100,height=90 )

    numero2 = tkinter.Label(vResultado, text=n2, bg="blue violet", font="Helvetica 47 bold")
    numero2.place(x=320, y=180,width=100,height=90 )

    resultado = tkinter.Label(vResultado, text=r, bg="blue violet", font="Helvetica 47 bold")
    resultado.place(x=480, y=180,width=200,height=90 )

    cs = tkinter.Label(vResultado, image=imgS)
    cs.place(x=250, y=200,width=50,height=50 )

    cr = tkinter.Label(vResultado, image=imgR)
    cr.place(x=430, y=200,width=50,height=50 )

    #----------------------- Etiquetas de fondo ------------------------

    f1 = tkinter.Label(vResultado, image=fondo, bg='blue violet', fg='blue violet')
    f1.place(x=0, y=410,width=160,height=160 )

    f2 = tkinter.Label(vResultado, image=fondo, bg='blue violet', fg='blue violet')
    f2.place(x=164, y=410,width=160,height=160 )
    
    f3 = tkinter.Label(vResultado, image=fondo, bg='blue violet', fg='blue violet')
    f3.place(x=328, y=410,width=160,height=160 )

    f4 = tkinter.Label(vResultado, image=fondo, bg='blue violet', fg='blue violet')
    f4.place(x=492, y=410,width=160,height=160 )
    
    f5 = tkinter.Label(vResultado, image=fondo, bg='blue violet', fg='blue violet')
    f5.place(x=656, y=410,width=160,height=160 )

    vResultado.mainloop()

#abrirVentanaSumaR(3,3,4)
#abrirVentanaRestaR(3,3,4)
#abrirVentanaMulR(3,4,5)
#abrirVentanaDivR(3,4,5)