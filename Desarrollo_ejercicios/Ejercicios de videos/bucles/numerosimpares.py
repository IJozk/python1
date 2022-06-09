#Crea un programa que muestre los números impares del 1 al 100. Los números deberánaparecer una al lado del otro sin salto de línea. 

numeros=""

for i in range(1,100,2):
    
    numeros=numeros+" "+str(i)
    
print(numeros)
    
    