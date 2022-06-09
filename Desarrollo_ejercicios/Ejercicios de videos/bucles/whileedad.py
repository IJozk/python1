edad=int(input("Introduce tu edad por favor."))

while edad<5 or edad>110:
    print("Edad incorrecta.")
    edad=int(input("Ingresa tu edad por favor."))
 
if edad<18:
   print("Eres menos de edad no puedes ingresar.")

else: 
  print("Gracias por colaborar. Puedes pasar.")
  print(f"Edad del aspirante: {edad} años")     