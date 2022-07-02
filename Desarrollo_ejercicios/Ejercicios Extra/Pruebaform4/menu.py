from funciones import *
import numpy as np

asientos1= np.arange(1,43,1).reshape(7,6).astype(str)
asientos2= np.arange(1,43,1).reshape(7,6).astype(str) # matriz memoria


cliente=["","","","",""]
seguir=True

while seguir:
    try:
        op=int(input("""Vuelos Duoc
                    Menú: 
        1. Ver asientos disponibles
        2.	Comprar asiento
        3.	Anular vuelo
        4.	Modificar datos de pasajero
        5.	Salir
        """))
    except:
        print("Opcion invalida.")
    
    if op==1:
        mostrarAsientos(asientos1)
    if op==2:
        cliente=ingresoDatosCliente(cliente)
        retorno=comprarAsiento(asientos1, cliente) 
        asientos1=retorno[0]
        cliente=retorno[1]
    if op==3:
        retorno=anularVuelo(asientos1, asientos2, cliente) 
        asientos1=retorno[0]   
        cliente=retorno[1]       
    if op==4:
        print(cliente)
        cliente=modificarDatos(cliente)
        print(cliente)
    if op==5:         
        seguir=False
