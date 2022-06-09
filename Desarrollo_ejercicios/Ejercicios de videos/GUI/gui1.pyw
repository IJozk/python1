from tkinter import *

raiz=Tk()

raiz.title("Ventana de pruebas.")

raiz.resizable(1,1) #Habilitar redimensionar

raiz.iconbitmap("freek.ico")

#raiz.geometry("650x350") #dar tamaño a la raiz

raiz.config(bg="green",relief="sunken", bd="35", cursor="hand1")

miFrame=Frame()

miFrame.pack()

#miFrame.pack(side="right", anchor="s")

#miFrame.pack(fill="both", expand="True")

miFrame.config(bg="red", width="650", height="350", relief="sunken", bd="35", cursor="pirate")

raiz.mainloop()