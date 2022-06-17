from tkinter import *

root=Tk()

root.title("Ejemplo")

playa=IntVar()
montagna=IntVar()
tRural=IntVar()

def opcionesViaje():
    
    opcionescogida="Usted ha escogido: "
    
    if(playa.get()==1):
        opcionescogida+=" playa"
        
    if(montagna.get()==1):
        opcionescogida+=" montaña"
    
    if(tRural.get()==1):
        opcionescogida+=" turismo rural"
        
    textoFinal.config(text=opcionescogida)            

foto=PhotoImage(file="Desarrollo_ejercicios/descarga.png")
Label(root, image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame, text="Elige destinos", width=50).pack()

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montaña", variable=montagna, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Turiamo rural", variable=tRural, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()

root.mainloop()