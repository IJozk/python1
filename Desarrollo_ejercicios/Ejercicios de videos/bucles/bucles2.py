from operator import truediv
contador1=0

contador2=0
email=False
miEmail=input("Introduzca su email.")

for i in miEmail:
    if (i=="."):
        contador1=contador1+1
    elif (i=="@"):
        contador2=contador2+1  

print(contador1)   
print(contador2)       
if contador1>=1 and  contador2==1:
    email=True        

if email:
    print("email correcto")
else:
    print("email incorrecto")            
        
        