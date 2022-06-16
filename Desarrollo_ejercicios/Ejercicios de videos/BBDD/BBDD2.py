import sqlite3

# Inicio conexión con BBDD
miConexion=sqlite3.connect("GestionDeProductos")

# Creación cursor
miCursor=miConexion.cursor()

# Crear tabla PRODUCTOS 
miCursor.execute('''
    CREATE TABLE PRODUCTOS(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
    PRECIO INTEGER,
    SECCION VARCHAR(20))                              
    ''')

# Tupla con datos de productos productos
productos=[
    
    ("Pelota",10000,"Juguetería"),
    ("Pantalón",14990,"Confección"),
    ("Destornillador",19990,"Ferretería"),
    ("Jarrón",30000,"Cerámica"),
    ("Pantalones",24990,"Confección")
]

# Insertar la tupla anterior a la tabla
miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)", productos)

miConexion.commit()

miConexion.close()