from tkinter import *

root=Tk()

miFrame=Frame(root, width=800, height=700)

miFrame.pack()

miImagen=PhotoImage(file="Desarrollo_ejercicios/tenor.gif")

#para ingresar texto en el label se utiliza text como parametro y para imagenes image.

Label(miFrame, image=miImagen, fg="red", font=("Comic Sans MS",18)).place(x=100, y=200)

root.mainloop()