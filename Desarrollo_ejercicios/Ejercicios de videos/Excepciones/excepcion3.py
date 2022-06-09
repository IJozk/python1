import math as m


def evaluaEdad(edad):
    
    """ La palabra clave raise permite lanzar un error cuando uno lo desee dentro del programa. Solo se pueden lanzar errores que se encuentren en la biblioteca de python, o de caso contrario si se desea crear un error propio se debe crear una clase (esto se vera mas adelante) """
    
    if edad<0:
        raise ZeroDivisionError("No se permiten edades negativas.")
    
    if edad<20:
        return "Eres muy joven"
    elif edad<40:
        return "Eres joven"
    elif edad<65:
        return "Eres maduro"
    elif edad<100:
        return "Cuidate.."
    

def raiz(num1):
    
    if num1<0:
        raise ValueError("El número no debe ser negativo.")
    else:
        return m.sqrt(num1)
    
op1=(int(input("Intruduce un numero: ")))    

""" Debemos capturar nuestro propio error que creamos para que el programa siga su ejecucion."""

try:
    print(f"La raiz de {op1} es: {raiz(op1)}")

except ValueError as ErrorDeNumeroNegativo:
    
    print(ErrorDeNumeroNegativo)    

print("Programa terminado.")

