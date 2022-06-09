def divide():
    
    """ Para un try se pueden agregar varios except. finally sirve para que al final una instruccion se ejecute si o si."""
    
    try:
        op1=(float(input("Introduce el primer numero: ")))
        op2=(float(input("Introduce el segundo numero: ")))
        print(f"La división de ambos numeros da como resultado: {op1/op2}")
    
    except ValueError:
        print("El valor introducido es erroneo.")
    
    except ZeroDivisionError:
        print("No se puede dividir por 0.")  
    
    finally:          
        print("Calculo finalizado.")
    
divide()    