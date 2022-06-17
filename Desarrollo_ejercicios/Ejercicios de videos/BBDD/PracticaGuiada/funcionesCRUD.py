import sqlite3
from tkinter import messagebox  

def conexion():
    try:
        miConexion=sqlite3.connect("Base_de_datos_clientes")
        
        cursor1=miConexion.cursor()
        
        cursor1.execute("""CREATE TABLE cliente (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR(100),
            PASS VARCHAR(10),
            APELLIDO VARCHAR(50),
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(200))""")
        
        miConexion.commit()
        
        miConexion.close()
    
    except:
        messagebox.showwarning("Atención","La base de datos ya fue creada.") 
        
  
        
    