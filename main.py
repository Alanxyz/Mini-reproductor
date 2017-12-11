from Tkinter import *
from pygame import mixer
from os import listdir
pausa = False
resume = True
numero = 0
lCanciones = []
nombre = "No hay canciones"
def filtro(canciones):                                       
    n = 0                                                    
    filtradas = []                                           
    limite = len(canciones)                                  
    while n < limite:
        if canciones[n][len(canciones[n])-3:] == 'mp3':      
            filtradas.append(canciones[n])                   
        n = n+1
    return filtradas
def lista():
    return listdir('.')
def cambiar():
    global nombre
    global canciones
    global numero
    global Nombret
    nombre = canciones[numero]
    Nombret = Label(ventana, text="\t\t\t\t\t").place(x=5, y=5)
    Nombret = Label(ventana, text=nombre).place(x=5, y=5)
def cancionAnterior():
    global numero
    global lcanciones
    n = numero - 1
    if n == -1:
        n = len(lcanciones) -1
    mixer.music.stop()
    mixer.music.load(lcanciones[n])
    mixer.music.play()
    numero = n
    cambiar()
def Accion():
    global pausa
    b = pausa
    if not b:
        if resume:
            mixer.music.play()
            global resume
            resume = False
        else:
            mixer.music.unpause()
    else:
        mixer.music.pause()
    pausa = not b
def cancionPosterior():
    global numero
    global lcanciones
    n = numero + 1
    if n == len(lcanciones):
        n = 0
    mixer.music.stop()
    mixer.music.load(lcanciones[n])
    mixer.music.play()
    numero = n
    cambiar()
mixer.init()
canciones = filtro(lista())
lcanciones = canciones
print canciones
nombre = canciones[numero]
ventana = Tk()
ventana.geometry("170x65")
ventana.resizable(width=FALSE, height=FALSE)
ventana.title("Reproductor")
mixer.music.load(canciones[0])
Nombret = Label(ventana, text=nombre).place(x=5, y=5)
anterior = Button(ventana, text="<-", command=cancionAnterior).place(x=10, y=25)
posterior = Button(ventana, text="->", command=cancionPosterior).place(x=120, y=25)
play = Button(ventana, text="Play", command=Accion).place(x=60, y=25)
ventana.mainloop()
