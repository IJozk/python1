import math

print("programa de calculo de raiz cuadrada.")
numero=int(input("Introduce un numero por favor."))

intentos=0

while numero<0:
    print("No se puede hallar la raíz de un numero negativo.")
    
    
    if intentos==2:
        print("Has ejecutado el programa demasiadas veces, ya no te quedan mas intentos. El programa ha finalizado.")
        break
    
    numero=int(input("Ingrese un numero por favor."))
    if numero<0:
        intentos=intentos+1

if intentos<2:
    solucion=math.sqrt(numero)
    print("La raiz cuadrada de "+ str(numero)+ " es "+str(solucion) + ".")