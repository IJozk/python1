from io import open_code

archivo_texto=open("archivo.txt","r")

texto=archivo_texto.read()

archivo_texto.close()

print(texto)



"""   *** Agregar una linea de texto***

archivo_texto=open("archivo.txt","a")

archivo_texto.write("\nsiempre es una buena ocasión para estudiar Python")

archivo_texto.close()

***Lectura de archivos***
1.-------
archivo_texto=open("archivo.txt","r")

texto=archivo_texto.read()

archivo_texto.close()

print(texto)

2.----
# readlines crea una lista en la cual contiene una cadena de texto correspondiente a cada linea del texto escrito.

lineas_texto=archivo_texto.readlines()

archivo_texto.close()

print(lineas_texto[:])
---------------

***Escritura de archivos***

archivo_texto=open("archivo.txt","w")

frase="Estupendo dia para estudiar Python \nel miercoles"

archivo_texto.write(frase)

archivo_texto.close()"""