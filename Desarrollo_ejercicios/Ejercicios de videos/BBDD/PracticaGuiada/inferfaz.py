from tkinter import * 
from tkinter import messagebox
from funcionesCRUD import *

root=Tk()

# Creamos el frame 
frame1=Frame(root, height=500, width=500)
frame1.pack()

# Creamos una barra de menu vacia
barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

# Menu BBDD
baseDeDatos=Menu(barraMenu, tearoff=0)
baseDeDatos.add_command(label="Conectar", command=conexion)
baseDeDatos.add_command(label="Salir")

# Menu Borrar
menuBorrar=Menu(barraMenu, tearoff=0)
menuBorrar.add_command(label='Borrar registro')

# Menu CRUD
menuCRUD=Menu(barraMenu, tearoff=0)
menuCRUD.add_command(label='Create')
menuCRUD.add_command(label='Read')
menuCRUD.add_command(label='Update')
menuCRUD.add_command(label='Delete')

# Menu Ayuda
menuAyuda=Menu(barraMenu, tearoff=0)
menuAyuda.add_command(label='Acerca de')
menuAyuda.add_command(label='Licencia')

# Barra menu
barraMenu.add_cascade(label="BBDD", menu=baseDeDatos)
barraMenu.add_cascade(label="Borrar", menu=menuBorrar)
barraMenu.add_cascade(label="CRUD", menu=menuCRUD)
barraMenu.add_cascade(label="Ayuda", menu=menuAyuda)

# Creamos los Labels y Entries, ademas de un cuadro de texto.
label1=Label(frame1, fg="blue", text="ID:", width=10, height=2)
label1.grid(column=0, row=0)

var_id=StringVar()
entryId=Entry(frame1, width=40, textvariable=var_id)
entryId.grid(column=1, row=0, columnspan=4, padx=20, pady=2)

label2=Label(frame1, fg="blue", text="Nombre:", width=10, height=2)
label2.grid(column=0, row=1)

var_nom=StringVar()
entryNom=Entry(frame1, width=40, textvariable=var_nom)
entryNom.grid(column=1, row=1, columnspan=4, padx=20, pady=2)

label3=Label(frame1, fg="blue", text="Pass:", width=10, height=2)
label3.grid(column=0, row=2)

var_pass=StringVar()
entryPass=Entry(frame1, width=40, textvariable=var_pass)
entryPass.grid(column=1, row=2, columnspan=4, padx=20, pady=2)

label4=Label(frame1, fg="blue", text="Apellido:", width=10, height=2)
label4.grid(column=0, row=3)

var_apell=StringVar()
entryApell=Entry(frame1, width=40, textvariable=var_apell)
entryApell.grid(column=1, row=3, columnspan=4, padx=20, pady=2)

label5=Label(frame1, fg="blue", text="Direccion:", width=10, height=2)
label5.grid(column=0, row=4)

var_dir=StringVar()
entryDir=Entry(frame1, width=40, textvariable=var_dir)
entryDir.grid(column=1, row=4, columnspan=4, padx=20, pady=2)

label6=Label(frame1, fg="blue", text="Comentarios:", width=10, height=2)
label6.grid(column=0, row=5)

cuadroComentarios=Text(frame1, width=30, height=10)
cuadroComentarios.grid(column=1, row=5, columnspan=4, padx=10, pady=2)

# Creación de botones

boton1=Button(frame1, text="Create", width=10, height=1)
boton1.grid(column=0, row=6)

boton2=Button(frame1, text="Read", width=10, height=1)
boton2.grid(column=1, row=6)

boton3=Button(frame1, text="Update", width=10, height=1)
boton3.grid(column=2, row=6)

boton4=Button(frame1, text="Delete", width=10, height=1)
boton4.grid(column=3, row=6)

root.mainloop()