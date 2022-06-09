def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):		
  
  #Con try el programa intentara realizar la operacion, si no lo logra por alguna razon, el programa ejecuta la instruccion except simpre que la excepcion sea la que se escribe dentro del codigo except(en este caso ZeroDivisionError). De no ser así el programa caera y no continuara ejecutandoce.
  
  try:	
    return num1/num2
  except ZeroDivisionError:
      print("No se puede dividir por 0")
      return "Operacion erronea."
  except  ValueError:
      print("valores incorrectos.") 

while True:
    try:
      op1=(int(input("Introduce el primer numero: ")))
      op2=(int(input("Introduce el segundo numero: ")))
      s=1/0
      break 
    except ValueError:
      print("Los valores introducidos no son correctos.")
    except ZeroDivisionError:
      print("No se puede dividir por 0")
  

             
	
operacion=input("Introduce la operacion a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operacion no contemplada")


print("Operacion ejecutada. Continuacion de ejecucion del programa ")