import sqlite3

# ******* CRUD *******

# Inicio conexión con BBDD
miConexion=sqlite3.connect("GestionDeProductos")

# Creación cursor
miCursor=miConexion.cursor()

# Leer informacionde la tabla
"""miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='Confección'")

productos=miCursor.fetchall()

print(productos)"""

# Updatear un registro
"""miCursor.execute("UPDATE PRODUCTOS SET PRECIO=3500 WHERE NOMBRE_ARTICULO='Pelota'")
"""

# Eliminar Registro
"""miCursor.execute("DELETE FROM PRODUCTOS WHERE NOMBRE_ARTICULO='Pantalones'")"""


miConexion.commit()

miConexion.close()