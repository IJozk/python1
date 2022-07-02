from tkinter import * 
from tkinter import messagebox
from funcionesCRUD import *


root=Tk()

# Funciones necesarias.
def salirAplicacion1():
    valor=salirAplicacion()
    if valor:
        root.destroy()  
def borrarRegistro():
        var_id.set("")
        var_user.set("")
        var_dir.set("")
        var_nom.set("")
        var_pass.set("")
        cuadroComentarios.delete('1.0', 'end-1c') 
def insertarUser():
    try:
        datos=var_user.get(),var_pass.get(),var_nom.get(),var_dir.get(),cuadroComentarios.get('1.0', 'end-1c')
        insertUser(datos)
        borrarRegistro()
    except:
        print("Problemas con la inserción de datos.")
def buscarUser(usuario):
    datos_usuario=buscar(usuario)
    var_id.set(datos_usuario[0][0])
    var_pass.set(datos_usuario[0][2])
    var_nom.set(datos_usuario[0][3])
    var_dir.set(datos_usuario[0][4])
    cuadroComentarios.delete('1.0', 'end-1c')
    cuadroComentarios.insert(END, f"{datos_usuario[0][5]}")  
def modificarUser():
    datos_cliente=var_user.get(),var_pass.get(),var_nom.get(),var_dir.get(),cuadroComentarios.get('1.0', 'end-1c'),var_id.get()
    modificar(datos_cliente) 
    borrarRegistro()   
def borrarUser():
    eliminarUnRegistro(var_id.get())
    borrarRegistro()




# Creamos el frame 
frame1=Frame(root, height=500, width=500)
frame1.pack()

# Creamos una barra de menu vacia
barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

# Menu BBDD
baseDeDatos=Menu(barraMenu, tearoff=0)
baseDeDatos.add_command(label="Conectar", command=conexion)
baseDeDatos.add_command(label="Borrar datos", command=lambda:alertaConfirm('borrarTodo','borrar todos los datos de la BBDD'))
baseDeDatos.add_command(label="Borrar tabla", command=lambda:alertaConfirm('borrarTabla','borrar la tabla de la BBDD'))
baseDeDatos.add_command(label="Salir", command=salirAplicacion1)

# Menu Borrar
menuBorrar=Menu(barraMenu, tearoff=0)
menuBorrar.add_command(label='Borrar registro', command=borrarRegistro)

# Menu CRUD
menuCRUD=Menu(barraMenu, tearoff=0)
menuCRUD.add_command(label='Create', command=insertarUser)
menuCRUD.add_command(label='Read', command=lambda:buscarUser(var_user.get()))
menuCRUD.add_command(label='Update', command=modificarUser)
menuCRUD.add_command(label='Delete', command=borrarUser)

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
entryId=Entry(frame1, width=40, textvariable=var_id, state="disabled")
entryId.grid(column=1, row=0, columnspan=4, padx=20, pady=2)

label2=Label(frame1, fg="blue", text="Usuario:", width=10, height=2)
label2.grid(column=0, row=1)

var_user=StringVar()
entryUser=Entry(frame1, width=40, textvariable=var_user)
entryUser.grid(column=1, row=1, columnspan=4, padx=20, pady=2)

label3=Label(frame1, fg="blue", text="Pass:", width=10, height=2)
label3.grid(column=0, row=2)

var_pass=StringVar()
entryPass=Entry(frame1, width=40, textvariable=var_pass)
entryPass.grid(column=1, row=2, columnspan=4, padx=20, pady=2)
entryPass.config(show="*")

label4=Label(frame1, fg="blue", text="Nombre comp:", width=10, height=2)
label4.grid(column=0, row=3)

var_nom=StringVar()
entryNom=Entry(frame1, width=40, textvariable=var_nom)
entryNom.grid(column=1, row=3, columnspan=4, padx=20, pady=2)

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

boton1=Button(frame1, text="Create", width=10, height=1, command=insertarUser)
boton1.grid(column=0, row=6)

boton2=Button(frame1, text="Read", width=10, height=1, command=lambda:buscarUser(var_user.get()))
boton2.grid(column=1, row=6)

boton3=Button(frame1, text="Update", width=10, height=1, command=modificarUser)
boton3.grid(column=2, row=6)

boton4=Button(frame1, text="Delete", width=10, height=1, command=borrarUser)
boton4.grid(column=3, row=6)

root.mainloop()