valido=True
password=input("Ingrese una contraseña.")

for i in range(len(password)):
    if password[i]==" ":
        valido=False

if   valido and len(password)>=8:
    print("Contraseña correcta.")   
else:
    print("Contraseña incorrecta.")          