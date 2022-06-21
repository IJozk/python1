from moduloCliente import *

#---------- Variables globales ----------
valOpc=True
valRut=True
valCelu=True
validIngr=True
validModificar=True
cambio=True  
x=1000

#---------- Opciones Menu ---------------
def menuPincipal():
    global valOpc
    valOpc=True
    #----------- Ciclo menu -----------------
    while valOpc:
        op1=int(input("Vuelos Duoc App:\n1. Registrar Cliente Nuevo.\n2. Ingresar con cuenta de cliente existente\n3. Salir\n"))
        if op1==1:
            registro()
            return globals()[f"cli{x}"]
        elif op1==2:
            returns=ingresar()
            valOpc=returns[0]
            return returns[1]
        elif op1==3:
            valOpc=False 
        else:
            print("Opcion incorrecta.")
            valOpc=True

#---------- Función registro ------------ 
def registro():
    global x
    global valRut
    global valCelu
    x=x+1
    #---------- Validar Rut --------------
    while valRut:
        try:
            rut=int(input("Ingresar rut: \n..."))
            if rut<4000000 or rut>99999999:
                print("Rut incorrecto, intentelo nuevamente.")
            else:
                print("Rut correcto.")
                valRut=False    
        except ValueError:
            print("Rut incorrecto, intentelo nuevamente.")
    #-------------------------------------
    nombre=input("Ingrese nombre:\n...")            
    #----------- Validar Celular ---------
    while valCelu:
        try:
            celular=int(input("Ingrese celular:\n..."))
            if celular<10000000 or celular>99999999:
                print("Celular incorrecto, intentelo nuevamente.")   
            else:
                valCelu=False        
        except ValueError:
            print("Celular incorrecto, intentelo nuevamente.")          
    #----------- Validar Tipo ------------
    banco=input("Ingrese el banco del cliente")
    
    #----------- Reset validadores -------
    valRut=True
    valCelu=True

    globals()[f"cli{x}"]=Cliente(str(rut),nombre,celular,banco)
    return globals()[f"cli{x}"]

#--------- Función suscripción ----------
def ingresar():
    global x
    global validIngr
    while validIngr:
        rutped=(input("Ingresar rut del cliente:\n"))
        for i in range(1000,x+1):
            if globals()[f"cli{i}"].rut==rutped:
                validIngr=False
                m=i
        if validIngr:
            print("Cliente no encontrado, intentelo nuevamente.")         
    if validIngr==False:
        print("Bienvenido ",globals()[f"cli{m}"].nombre)
        validIngr=True
        return False ,  globals()[f"cli{m}"] 
              
#--------- Función consulta -------------
def modificar():
    global cambio
    global validModificar
    while validModificar:
        try:
            rutped=(input("Ingresar rut del cliente a suscribir:\n"))
            for i in range(1000,x+1):
                if globals()[f"cli{i}"].rut==rutped:
                    validModificar=False
                    m=i
                    break
            if validModificar:
                print("Cliente no encontrado, intentelo nuevamente.")
            else:
                globals()[f"cli{m}"].mostrarDatos()  
        except:
            print("Cliente no encontrado.")
        while cambio:    
            opc1=input("Elija que dato desea modificar: \n1. Nombre usuario.\n2. Telefono usuario.\n3. Cancelar.")
            if opc1=="1":
                nombre=input("Escriba el nuevo nombre de usuario.")
                globals()[f"cli{m}"].nombre=nombre
                cambio=False
            elif opc1=="2":
                celular=input("Escriba el nuevo telefono celular del usuario.")
                globals()[f"cli{m}"].celular=celular
                cambio=False
            elif opc1=="3":
                print("No se han realizado cambios.")
                cambio=False
            else:
                print("Opción ingresada no valida.")        
                  
    cambio=True             
    validModificar=True               
           
#----------- Cliente de prueba ----------
cli1000=Cliente("12345678", "Cliente prueba", 12345678, "BancoDuoc")
