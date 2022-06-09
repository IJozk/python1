numero1=int(input("Ingrese un numero."))
numero2=int(input("Ingrese un segundo numero."))
mayor=0
    
def devuelvemax(numero1,numero2):
    list1=[numero1, numero2]
    print(numero1)
    print(numero2)
    if numero1>=numero2:
            mayor=numero1
            return print("El numero mayor es:", mayor)
    else:
            mayor=numero2
            return print("El numero mayor es:", mayor)
    
devuelvemax(numero1, numero2)
             

   
           