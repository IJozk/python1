palabra=input("Ingrese una palabra.")

contA=0

#----- Recorrer string ------
#----- Forma 1 --------------
for i in palabra:
    if i=="a":
        contA+=1 # contA+=1 ==> contA=contA + 1
print(f"La palabra que ingresaste tiene {contA} letras a.")
contA=0

#----- Forma 2 --------------

for i in range(0, len(palabra)):
        if palabra[i]=="a":
            contA+=1 # contA+=1 ==> contA=contA + 1
print(f"La palabra que ingresaste tiene {contA} letras a.")  





      
        