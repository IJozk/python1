import math

# funcion para mostrar asientos.
def mostrar_asientos(asientos1):
    matriz_asientos=''
    for i in range(0,7):
        if i==0:
            matriz_asientos=matriz_asientos+f'| {asientos1[i][0]}  {asientos1[i][1]}  {asientos1[i][2]}       {asientos1[i][3]}  {asientos1[i][4]}  {asientos1[i][5]}  |\n|                        |\n'
        elif i==1:
            matriz_asientos=matriz_asientos+f'| {asientos1[i][0]}  {asientos1[i][1]}  {asientos1[i][2]}       {asientos1[i][3]} {asientos1[i][4]} {asientos1[i][5]} |\n|                        |\n'
        elif i==4:
            matriz_asientos=matriz_asientos+f'| {asientos1[i][0]} {asientos1[i][1]} {asientos1[i][2]}      {asientos1[i][3]} {asientos1[i][4]} {asientos1[i][5]} |\n|_________      _________|\n|_________      _________|\n'            
        else:
            matriz_asientos=matriz_asientos+f'| {asientos1[i][0]} {asientos1[i][1]} {asientos1[i][2]}      {asientos1[i][3]} {asientos1[i][4]} {asientos1[i][5]} |\n|                        |\n'
                
    return matriz_asientos 

# Funciones del menú
def compra(cliente, asientos1, asientos2):
            valor_pasaje=0
            try:    
                asient_eleg=int(input("Ingrese el numero de asiento disponible que desea comprar:"))
                print(cliente.banco.lower())
                if cliente.banco.lower()=="bancoduoc":
                    if asient_eleg<31:
                        valor_pasaje=78000*0.85
                    elif asient_eleg>=31:
                        valor_pasaje=240000*0.85   
                else:
                    if asient_eleg>=31:
                        valor_pasaje=78000
                    elif asient_eleg<31:
                        valor_pasaje=240000
                confirm=input(f"El valor del pasaje es de {valor_pasaje}¿Deseas continuar?\n1. Si\n2. No\n")
                if confirm=="1":           
                    x=math.floor((asient_eleg-1)/6)
                    y=asient_eleg%6-1
                    if asientos1[x][y]==str(asient_eleg):
                        if asient_eleg>10:
                            asientos1[x][y]=' X'
                            asientos2[x][y]= cliente.rut
                        else:
                            asientos1[x][y]='X'
                            asientos2[x][y]= cliente.rut
                    elif asientos1[x][y]=='X' or asientos1[x][y]==' X':
                        print("asiento ocupado")        
                    else:
                        print("Numero de asiento no valido.")
                    print("\n")    
                    print(f"|---------Pasaje------------|\n|Cliente: {cliente.nombre}       |\n|Rut cliente: {cliente.rut}      |\n|Fono contacto: {cliente.celular}    |\n|Asiento: {asient_eleg}                |\n|Valor pasaje: {valor_pasaje}       |\n|Banco: {cliente.banco}           |\n")             
                    return asientos1, asientos2
                elif confirm=="2":
                    pass
            except ValueError:
                print("Has ingresado un dato incorrectamente, intenta con un numero entero.")
def anular(cliente,asientos1,asientos2):   
            try: 
                asient_eleg=int(input("Ingrese el numero de asiento del pasaje que desea anular:"))
                x=math.floor((asient_eleg-1)/6)
                y=asient_eleg%6-1
                if cliente.rut==asientos2[x][y]:    
                    if asientos1[x][y]=='X' or asientos1[x][y]==' X':
                            asientos1[x][y]=f'{asient_eleg}'
                            asientos2[x][y]=f'{asient_eleg}'        
                else:
                        print("Numero de asiento y el cliente no coinciden.")         
                return asientos1,asientos2
            except ValueError:
                print("Has ingresado un dato incorrectamente, intenta con un numero entero.") 
def modificarPasaje(cliente,asientos2):   
            asient_eleg=int(input("Ingrese el numero de asiento del pasaje que desea anular:"))
            x=math.floor((asient_eleg-1)/6)
            y=asient_eleg%6-1
            if cliente==asientos2[x][y]:
                return True
            else:
                return False
