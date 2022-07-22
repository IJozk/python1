def funcion_decoradora(funcion_parametro):

    """Esta es un decorador de funciones."""

    def funcion_interior():

        a=int(input("\nIngrese un número.    "))
        b=int(input("\nIngrese un segundo número.    "))

        funcion_parametro(a,b)

        print("Se ha realizado el calculo con exito.\n")

    return funcion_interior

@funcion_decoradora
def suma(a,b):

    print(f"\nEl resultado de la  suma es de {a+b}\n")

@funcion_decoradora
def resta(a,b):

    print(f"\nEl resultado de la  resta es de {a-b}\n")

# Menu 

help(funcion_decoradora)

seguir=True

while seguir:
    try:
        opc=int(input("Ingrese una de las siguientes opciones: \n1. Suma \n2. Resta\n3. Salir\n"))
        if opc==1:
            suma()
        elif opc==2:
            resta()
        else:
            seguir=False        

    except:
        print("Opcion incorrecta, intentelo nuevamente.")


