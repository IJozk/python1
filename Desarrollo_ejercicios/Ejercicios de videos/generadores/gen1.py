""""Un generador construye un objeto generador, en el cual se van generando uno a uno elementos (tuplas, palabras, numeros, etc) dentro de ese objeto por cada iteracion."""

def generapares(limite):
    
    num=1
    
    while num<limite:
        
        #y
        yield num*2
        
        num=num+1
        

miLista=generapares(10)

print(next(miLista))  

#suspencion

print("mas codigo...") 

print(next(miLista)) 

#suspencion

print("mas codigo...") 

print(next(miLista))    