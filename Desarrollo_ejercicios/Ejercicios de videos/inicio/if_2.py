#print("Verificacion de acceso")

#edad_usuario=int(input("Introduce tu edad, por favor"))

#if edad_usuario<18:
 #   print("No puedes pasar")
#elif edad_usuario>100:
 #   print("Edad erronea")    
#else:
  #  print("Puedes pasar")
    
#print("Fin del programa")            



print("Calificaciones.")

nota_usuario=int(input("Introduce tu nota, por favor"))

if nota_usuario<0 or nota_usuario>10:
    print("Nota ingesada incorrecta")  
elif nota_usuario<5:
    print("Insuficiente")
elif nota_usuario<6:
    print("Suficiente")
elif nota_usuario<7:
    print("Bien")   
elif nota_usuario<9:
    print("Notable")   
   
  
else:
    print("Sobresaliente")
    
print("Fin del programa")