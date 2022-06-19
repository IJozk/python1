import sqlite3
from tkinter import messagebox 


def conexion():
    try:
        miConexion=sqlite3.connect("Base_de_datos_clientes")
        
        cursor1=miConexion.cursor()
        
        cursor1.execute("""CREATE TABLE cliente (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            USUARIO VARCHAR(100) UNIQUE NOT NULL,
            PASS VARCHAR(10) NOT NULL,
            NOMBRE_COMPLETO VARCHAR(50) NOT NULL,
            DIRECCION VARCHAR(50) NOT NULL,
            COMENTARIOS VARCHAR(200));""")
        
        miConexion.commit()
        
        miConexion.close()
    
    except:
        messagebox.showwarning("Atención","La base de datos ya fue creada.") 
        
def salirAplicacion():
    valor=messagebox.askokcancel("Salir", "¿Deseas salir de la aplicación?") # Entrega de vuelta los valores booleanos True o False
    return valor

def borrarTodo():
        miConexion=sqlite3.connect("Base_de_datos_clientes")
        
        cursor1=miConexion.cursor()
        
        cursor1.execute("DELETE FROM cliente ;")
        
        miConexion.commit()
        
        miConexion.close()

def borrarTabla():
        miConexion=sqlite3.connect("Base_de_datos_clientes")
        
        cursor1=miConexion.cursor()
        
        cursor1.execute("DROP TABLE cliente ;")
        
        miConexion.commit()
        
        miConexion.close()      
        
def alertaConfirm(accion,mensaje):
    valor=messagebox.askokcancel("Salir", f"Usted esta apunto de {mensaje}, ¿Desea continuar?") # Entrega de vuelta los valores booleanos True o False
    if valor: 
        if accion=="borrarTodo":
            borrarTodo()
        if accion=="borrarTabla":
            borrarTabla() 
    else:
        pass           


# Funciones CRUD

# Create
def insertUser(user):
    try:
        miConexion=sqlite3.connect("Base_de_datos_clientes")
            
        cursor1=miConexion.cursor()
            
        cursor1.execute(f"{user}")
            
        miConexion.commit()
            
        miConexion.close()
    
    except:
        ("Problemas con la inserción de datos.")        

# Read
def buscar(usuario):
    try:
        miConexion=sqlite3.connect("Base_de_datos_clientes")
            
        cursor1=miConexion.cursor()
            
        cursor1.execute(f"SELECT * FROM cliente WHERE USUARIO='{usuario}';")
        
        datosUsuario=cursor1.fetchall()
            
        miConexion.commit()
            
        miConexion.close()
        
        return datosUsuario
        
    except:
        ("Problemas con la busqueda de datos.") 
        messagebox.showwarning("Atención","No se han encontrado coincidencias.")  
        
# Update
def modificar(datos_cliente):
    try:
        miConexion=sqlite3.connect("Base_de_datos_clientes")
            
        cursor1=miConexion.cursor()
            
        cursor1.execute(f"UPDATE cliente SET usuario='{datos_cliente[1]}', pass='{datos_cliente[2]}', nombre_completo='{datos_cliente[3]}', direccion='{datos_cliente[4]}', comentarios='{datos_cliente[5]}' WHERE ID='{datos_cliente[0]}';")
        
        datosUsuario=cursor1.fetchall()
            
        miConexion.commit()
            
        miConexion.close()
        
        return datosUsuario
        
    except:
        ("Problemas con la busqueda de datos.")
        messagebox.showwarning("Atención","No se han encontrado coincidencias.")   


# Delete                       
def eliminarUnRegistro(id_user):
    try:
        miConexion=sqlite3.connect("Base_de_datos_clientes")
            
        cursor1=miConexion.cursor()
            
        cursor1.execute(f"DELETE FROM cliente WHERE ID='{id_user}';")
        
        datosUsuario=cursor1.fetchall()
            
        miConexion.commit()
            
        miConexion.close()
        
        return datosUsuario
        
    except:
        ("Problemas con la busqueda de datos.")  
        messagebox.showwarning("Atención","No se han encontrado coincidencias.") 