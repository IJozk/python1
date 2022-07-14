from funciones import *

asientos1=crearMatriz()

num=input("Ingrese un numero del 1 al 24")

asientos1=asientoOcupado(num, asientos1)
            
asientosOrdenados=guardarCambios(asientos1) 
            
print(asientosOrdenados)            
        