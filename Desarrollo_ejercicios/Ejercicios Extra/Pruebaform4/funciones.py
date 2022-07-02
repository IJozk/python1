def suma():
    
    a=int(input("Ingrese el primer numero a sumar.\n"))
    b=int(input("Ingrese el segundo numero a sumar.\n")) 
    suma=a+b
    return suma

def mostrarAsientos(asientos1):
    masientos=f"""|	{asientos1[0][0]}	{asientos1[0][1]}	{asientos1[0][2]}		{asientos1[0][3]}	{asientos1[0][4]}	{asientos1[0][5]}	|
|								|
|	{asientos1[1][0]}	{asientos1[1][1]}	{asientos1[1][2]}		{asientos1[1][3]}	{asientos1[1][4]}	{asientos1[1][5]}	|
|								|
|	{asientos1[2][0]}	{asientos1[2][1]}	{asientos1[2][2]}		{asientos1[2][3]}	{asientos1[2][4]}	{asientos1[2][5]}	|
|								|
|	{asientos1[3][0]}	{asientos1[3][1]}	{asientos1[3][2]}		{asientos1[3][3]}	{asientos1[3][4]}	{asientos1[3][5]}	|
|								|
|	{asientos1[4][0]}	{asientos1[4][1]}	{asientos1[4][2]}		{asientos1[4][3]}	{asientos1[4][4]}	{asientos1[4][5]}	|
|______________________                 ________________________|
|______________________                 ________________________|
|	{asientos1[5][0]}	{asientos1[5][1]}	{asientos1[5][2]}		{asientos1[5][3]}	{asientos1[5][4]}	{asientos1[5][5]}	|
|								|
|								|
|	{asientos1[6][0]}	{asientos1[6][1]}	{asientos1[6][2]}		{asientos1[6][3]}	{asientos1[6][4]}	{asientos1[6][5]}	|
"""
    print(masientos)

def ingresoDatosCliente(cliente):
    nombre=input("Ingrese su nombre")
    run=int(input("Ingrese su run"))
    telefono=input("Ingrese su numero telefonico")
    banco=input("Ingrese su banco")
    
    cliente=[nombre, run, telefono, banco, "0"]
    
    return cliente


def comprarAsiento(asientos1, cliente):
    asiento=input("Ingrese el numero de asiento que desee.\n")
    for i in range(7):
        for j in range(6):
            if asiento==asientos1[i][j]:
                valor=valorAsiento(cliente, asiento)
                dcliente=input(f"El valor del pasaje es de {valor} ¿Desea realizar la compra?.\n1. Si \n2. No")
                if dcliente=="1":
                    asientos1[i][j]='X'
                    cliente[4]=asiento
                    print(cliente)
                asientoencontrado=True
    if int(asiento)>42 or int(asiento)<1:
        print("El asiento ingresado no existe.")                         
    elif asientoencontrado==False:
        print("El asiento ingresado no esta disponible.")  
    return asientos1, cliente
                
def valorAsiento(cliente, asiento):
    if cliente[3]=="BancoDuoc":
        if int(asiento)<=30:
            valorpasaje=78900*0.85
        elif int(asiento)>30:
            valorpasaje=240000*0.85
    elif cliente[3]!="BancoDuoc":
        if int(asiento)<=30:
            valorpasaje=78900
        elif int(asiento)>30:
            valorpasaje=240000            

    return valorpasaje


def anularVuelo(asientos1,asientos2,cliente):
    anulasiento=input("Ingrese el asiento a anular\n")
    if anulasiento==cliente[4]:
        for i in range(7):
            for j in range(6):
                if anulasiento==asientos2[i][j]:
                    asientos1[i][j]=asientos2[i][j]
                    cliente=[]
                    asientoencontrado=True
        if int(anulasiento)>42 or int(anulasiento)<1:
            print("El asiento ingresado no existe.")                         
        elif asientoencontrado==False:
            print("El asiento ingresado no esta disponible.")  
    return asientos1, cliente

def modificarDatos(cliente):
    run=int(input("Ingrese el run del cliente\n"))
    asiento=input("Ingrese el asiento asignado al cliente\n")
    if run==cliente[1] and asiento==cliente[4]:
        opc=int(input("Menu modificar cliente. \n1. Modificar nombre.\n2. Modificar telefono.\n3. Salir"))
        if opc==1:
            nombre=input("Ingrese el nombre del cliente para modificación.")
            cliente[0]=nombre
        elif opc==2:
            telefono=input("Ingrese el telefono del cliente para modificación.")
            cliente[2]=telefono
        elif opc==3:
            print("No se han realizado cambios")
        else:
            print("Opcion invalida.")           
    return cliente    


