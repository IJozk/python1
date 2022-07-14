import numpy as np

def crearMatriz():
    asientos1= np.arange(1,25,1).reshape(6,4).astype(str)
    return asientos1

def guardarCambios(asientos1):
    asientosOrdenados=""
    for i in range(6):
        for j in range(4):
            if j==0:
                asientosOrdenados=asientosOrdenados+"| "+ asientos1[i][j]
            elif j==3:
                asientosOrdenados=asientosOrdenados+" "+ asientos1[i][j]+" |\n"
            else :
                asientosOrdenados=asientosOrdenados+ " "+asientos1[i][j]
    
    return asientosOrdenados 

def asientoOcupado(numAsiento, asientos1):
    for i in range(6):
        for j in range(4):
            if asientos1[i][j]==numAsiento:
                asientos1[i][j]="x"
                
    return asientos1            
                    