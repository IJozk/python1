#metodos de strings

nombreUsuario=input("Introduce tu nombre de usuario.")
#upper()
print(f"El nombre en mayusculas: {nombreUsuario.upper()}")
#lower()
print(f"El nombre en minusculas: {nombreUsuario.lower()}")
#capitalize
print(f"El nombre con la primera letra mayuscula: {nombreUsuario.capitalize()}")
#isdigit
edad=input("Introduce tu edad: ")
print(edad.isdigit())

while edad.isdigit()==False:
    print("Por favor introduce un valor numerico.")
    edad=input("Introduce tu edad: ")

if (int(edad)<18):
    print("No puedes pasar.")
    
else:
    print("Puedes pasar.")    