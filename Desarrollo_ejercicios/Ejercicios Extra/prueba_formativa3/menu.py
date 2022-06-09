from moduloCliente import *

#---------- Variables globales ----------
valOpc=True
valRut=True
valEdad=True
valGen=True
valCelu=True
valCorr=True
valTip=True
validConsulta=True
validSus=True
x=1000

#---------- Opciones Menu ---------------

def menuPincipal():
    op1=int(input("Juan Maestro App:\n1. Registrar Cliente\n2. Suscripcion\n3. Consultar Datos Cliente\n4. Salir\n"))
    return op1

#---------- Función registro ------------ 

def registro():
    global x
    global valOpc
    global valRut
    global valEdad
    global valGen
    global valCelu
    global valCorr
    global valTip
    global validConsulta
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
    direccion=input("Ingrese direccion:\n...")
    comuna=input("Ingrese comuna:\n...")
    #---------- Validar Correo -----------
    while valCorr:
        try:
            contArroba=0
            contLetra=0
            correo=input("Ingrese correo:\n...")
            for i in correo:
                if i=="@":
                    contArroba=contArroba+1
                    contLetra=0 
                else:
                    contLetra=contLetra+1            
            if correo[0]=="@" or correo[len(correo)-1]=="@" or contLetra<1 or correo[len(correo)-1]=="." or correo[len(correo)-2]=="." or (correo[len(correo)-3]=="." and correo[len(correo)-4]!=".") or correo[len(correo)-5]=="." or contArroba>1:
                print("Correo incorrecto, intentelo nuevamente.")
            else:
                valCorr=False
                print("Correo correcto.")      
                            
        except ValueError:
            print("Correo incorrecto, intentelo nuevamente.")    
    #----------- Validar Edad ------------ 
    while valEdad:
        try:
            edad=int(input("Ingresar edad: \n..."))
            if edad<=0 or edad>110:
                print("Edad incorrecto, intentelo nuevamente.")
            else:
                valEdad=False
                print("Edad correcta.")    
        except ValueError:
            print("Edad incorrecto, intentelo nuevamente.")
    #----------- Validar Genero ----------
    while valGen:
        try:
            genero=input("Ingresar genero: (m para masculino y f para femenino) \n...").lower()
            if genero=="m" or genero=="f":
                print("Genero correcto.")
                valGen=False 
            else:
                print("Genero incorrecto, intentelo nuevamente.")    
        except ValueError:
            print("Genero incorrecto, intentelo nuevamente.")                 
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
    while valTip:
        try:
            tipo=input("Ingresar tipo: Premiun, Gold o Silver. \n...").upper()
            if tipo=="PREMIUN" or tipo=="GOLD" or tipo=="SILVER":
                print("Tipo correcto.")
                valTip=False 
            else:
                print("Tipo incorrecto, intentelo nuevamente.")    
        except ValueError:
            print("Tipo incorrecto, intentelo nuevamente.")   
    #----------- Reset validadores -------
    valRut=True
    valEdad=True
    valGen=True
    valCelu=True
    valCorr=True
    valTip=True
    
    
    globals()[f"cli{x}"]=Cliente(str(rut),nombre,direccion,comuna,correo,edad,genero,celular,tipo)
    consult()

#--------- Función suscripción ----------
def suscr():
    global x
    global validSus
    while validSus:
        rutped=(input("Ingresar rut del cliente a suscribir:\n"))
        for i in range(1000,x+1):
            if globals()[f"cli{i}"].rut==rutped:
                validSus=False
                m=i
        if validSus:
            print("Cliente no encontrado, intentelo nuevamente.")        
    fecha=input("Ingrese fecha: (En el formato xx/xx/xx)\n")    
    if validSus==False:
        globals()[f"cli{m}"].suscripcion=(globals()[f"cli{m}"].suscripcion,("suscrito",f"{fecha}"))
        validSus=True
            
#--------- Función consulta -------------
def consult():
    global validConsulta
    while validConsulta:
        try:
            rutped=(input("Ingresar rut del cliente a suscribir:\n"))
            for i in range(1000,x+1):
                if globals()[f"cli{i}"].rut==rutped:
                    validConsulta=False
                    m=i
                    break
            if validConsulta:
                print("Cliente no encontrado, intentelo nuevamente.")
            else:
                globals()[f"cli{m}"].mostrarDatos()  
        except:
            print("Cliente no encontrado.") 
    validConsulta=True               

            
#----------- Cliente de prueba ----------
cli1000=Cliente("12345678", "prueba", "prueba", "prueba","prueba", "prueba", "prueba", "prueba","prueba")

#----------- Ciclo menu -----------------
while valOpc:
    op1=menuPincipal()
    if op1==1:
        registro()
    elif op1==2:
        suscr()
    elif op1==3:
        consult() 
    elif op1==4:
        print("Gracias por suscribirse a la App de Juan Maestro...")
        valOpc=False 
    else:
        valOpc=True

               