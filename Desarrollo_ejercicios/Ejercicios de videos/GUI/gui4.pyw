from cgitb import text
from tkinter import *

root=Tk()

miFrame=Frame(root, width=1200, height=600)
miFrame.pack()

miNombre=StringVar()

# ---- Entrys ----

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=0, column=1, padx= 10, pady=10)
cuadroNombre.config(fg="red", justify="right")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1, column=1, padx= 10, pady=10)

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=2, column=1, padx= 10, pady=10)
cuadroPass.config(show="$")

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx= 10, pady=10)

# ------ Texts ------

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=4, column=1, pady=10, padx=10)

scrollvert=Scrollbar(miFrame, command=textoComentario.yview)
scrollvert.grid(row=4, column=2, sticky="nsew")

textoComentario.config(yscrollcommand=scrollvert.set)


# ----- Labels -----

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="w", padx= 10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=1, column=0, sticky="w", padx= 10, pady=10)

direccionLabel=Label(miFrame, text="Direccion:")
direccionLabel.grid(row=3, column=0, sticky="w", padx= 10, pady=10)

passLabel=Label(miFrame, text="Password")
passLabel.grid(row=2, column=0, sticky="w", padx= 10, pady=10)

comentarioLabel=Label(miFrame, text="Comentarios:")
comentarioLabel.grid(row=4, column=0, sticky="w", padx= 10, pady=10)

# ----- Buttons ----

def codigoBoton():
    
    miNombre.set("Jorge")

botonEnvio=Button(root, text="Enviar", command=codigoBoton)
botonEnvio.pack()

root.mainloop()