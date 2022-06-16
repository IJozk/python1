import sqlite3

miConexion=sqlite3.connect("BaseDeDatosPrueba")

miCursor=miConexion.cursor()

#miCursor.execute("CREATE TABLE PRODUCTOS (nom_art varchar(100), precio integer, seccion varchar(50))")

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('Balón', 10000, 'Deportes')")

"""variosProductos=[
    ("Camisa", 1000,"Ropa Hombre"), 
    ("Chutiador", 20000,"Deportes"),  
    ("PC Gamer", 1000000,"PC")  
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)", variosProductos)"""

miCursor.execute("select * from PRODUCTOS")

variosProductos=miCursor.fetchall()

for producto in variosProductos:
    print(f"Nombre del articulo: {producto[0]}\nPrecio:  {producto[1]}\nSeccion: {producto[2]}\n------------------")

miConexion.commit()

miConexion.close()