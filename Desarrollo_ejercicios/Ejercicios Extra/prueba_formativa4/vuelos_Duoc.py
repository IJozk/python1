from funciones_vuelos_duoc import *
import numpy as np
from menu import *

seguir=True
returns=("","")

asientos1= np.arange(1,43,1).reshape(7,6).astype(str)
asientos2= np.arange(1,43,1).reshape(7,6).astype(str)

print("Bienvenido a el sistema de compra de pasajes Vuelos_DUOC.")

# Menu
while seguir:
    try:
        opc=int(input("""Ingrese una de las siguientes opciones:
        1.	Ver asientos disponibles
        2.	Comprar asiento
        3.	Anular vuelo
        4.	Modificar datos de pasajero
        5.	Salir
        """))
        print("\n")
        if opc==1:
            print(mostrar_asientos(asientos1))       
        elif opc==2:
            cliente=menuPincipal()
            returns=compra(cliente, asientos1, asientos2)
            asientos1=returns[0]
            asientos2=returns[1]
        elif opc==3:
            returns=ingresar()
            cliente=returns[1]
            anular(cliente,asientos1,asientos2)    
        elif opc==4:
            rut=input("Ingrese el rut del cliente.") 
            valid=modificarPasaje(rut)
            if valid:
                modificar()
    except:
        print("Valor no valido, intentelo nuevamente.")

# Codigo en deshuso    
"""    if returns[1]=="":
        seguir=returns[0]
        returns=("","")
    else: 
        seguir=returns[0]
        asientos2=returns[1]
        returns=("","")
    # Constructor de orden de asientos.
for i in range(14):
    listan.append(count+1)
    listan.append(count+2)
    listan.append(count+3)
    asientos2.append(listan)
    count=count+3
    listan=[]    
        """
        