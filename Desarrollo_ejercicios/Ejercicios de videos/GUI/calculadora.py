from pydoc import text
from tkinter import *
from tkinter import font
from tkinter.tix import TEXT

root=Tk()

miFrame=Frame(root)
miFrame.pack()

simb=StringVar()
    
nombreCalc=Label(miFrame, text="Cassiopemas")
nombreCalc.grid(row=0, column=2)

#------ Pantalla ------

numeroPantalla=StringVar()

miPantalla=Entry(miFrame, textvariable=numeroPantalla)
miPantalla.grid(row=1,column=0, columnspan=5,rowspan=1 , padx=5, pady=5)
miPantalla.config(bg="black", fg="white", justify="right", width=40 ,)

#--------- Pulsar botones y demás funciones ----------------

def pulsarBoton(tecla):
    if numeroPantalla.get()=="0":
        if tecla=="0" or tecla=="+" or tecla=="-" or tecla=="*" or tecla=="/":
            numeroPantalla.set("0")
        else:
            numeroPantalla.set(tecla)            
    else:        
        numeroPantalla.set(numeroPantalla.get()+tecla)
    
def calculo():
    calc=eval(str(numeroPantalla.get()))
    numeroPantalla.set(str(calc))  
    
def borrarPantalla():
    numeroPantalla.set("0")      

    
# ---- Botones  numericos ------
boton7=Button(miFrame, text="7", width=3, command=lambda:pulsarBoton("7"))
boton7.grid(row=2, column=0, padx=5, pady=5)
boton7.config(font=10)
boton8=Button(miFrame, text="8", width=3, command=lambda:pulsarBoton("8"))
boton8.grid(row=2, column=1, padx=5, pady=5)
boton8.config(font=10)
boton9=Button(miFrame, text="9", width=3, command=lambda:pulsarBoton("9"))
boton9.grid(row=2, column=2, padx=5, pady=5)
boton9.config(font=10)
boton4=Button(miFrame, text="4", width=3, command=lambda:pulsarBoton("4"))
boton4.grid(row=3, column=0, padx=5, pady=5)
boton4.config(font=10)
boton5=Button(miFrame, text="5", width=3, command=lambda:pulsarBoton("5"))
boton5.grid(row=3, column=1, padx=5, pady=5)
boton5.config(font=10)
boton6=Button(miFrame, text="6", width=3, command=lambda:pulsarBoton("6"))
boton6.grid(row=3, column=2, padx=5, pady=5)
boton6.config(font=10)
boton1=Button(miFrame, text="1", width=3, command=lambda:pulsarBoton("1"))
boton1.grid(row=4, column=0, padx=5, pady=5)
boton1.config(font=10)
boton2=Button(miFrame, text="2", width=3, command=lambda:pulsarBoton("2"))
boton2.grid(row=4, column=1, padx=5, pady=5)
boton2.config(font=10)
boton3=Button(miFrame, text="3", width=3, command=lambda:pulsarBoton("3"))
boton3.grid(row=4, column=2, padx=5, pady=5)
boton3.config(font=10)
boton0=Button(miFrame, text="0", width=3, command=lambda:pulsarBoton("0"))
boton0.grid(row=5, column=1, padx=5, pady=5)
boton0.config(font=10)

# ---- Botones  operaciones matematicas ------

botonmas=Button(miFrame, text="+", width=3, command=lambda:pulsarBoton("+"))
botonmas.grid(row=5, column=3, sticky="s",padx=5, pady=5)
botonmas.config(font=10)

botonmenos=Button(miFrame, text="-", width=3,command=lambda:pulsarBoton("-"))
botonmenos.grid(row=4, column=3, sticky="s",padx=5, pady=5)
botonmenos.config(font=10)

botonmult=Button(miFrame, text="X", width=3, command=lambda:pulsarBoton("*"))
botonmult.grid(row=3, column=3, sticky="s",padx=5, pady=5)
botonmult.config(font=10)

botondiv=Button(miFrame, text="/", width=3, command=lambda:pulsarBoton("/"))
botondiv.grid(row=2, column=3, sticky="s",padx=5, pady=5)
botondiv.config(font=10)

botonigual=Button(miFrame, text="=", width=3, command=calculo)
botonigual.grid(row=5, column=2, sticky="s",padx=5, pady=5)
botonigual.config(font=10)

botonclc=Button(miFrame, text="C", width=3, command=borrarPantalla)
botonclc.grid(row=5, column=0, sticky="s",padx=5, pady=5)
botonclc.config(font=10)



root.mainloop()