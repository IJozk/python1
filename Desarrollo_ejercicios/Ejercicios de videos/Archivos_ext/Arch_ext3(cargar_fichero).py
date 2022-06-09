import pickle

#Cargar datos desde ficheros binarios.

fichero=open("lista_nombres", "rb")

lista=pickle.load(fichero)

print(lista)
