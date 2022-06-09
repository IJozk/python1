while True:
    try:
        opc=int(input("------- Menu ------ \n1. Registrar. \n2. Suscribir. \n 3. Consultar \n4. Salir"))    
    except ValueError:
        print("Opcion incorrecta, intentelo nuevamente.")
        continue
            
    if opc==1:
        # ----------------- Validar Rut ------------------------
        while True:
            try:
                rut=int(input("Ingresar rut del cliente. \n"))
                if rut>=4000000 and rut<=99999999:
                    print("Rut correcto.")
                    break
                else:
                    print("Rut incorrecto.")
            except ValueError:
                print("Rut incorrecto, ingreso un valor no valido. Intentelo nuevamente.")         
            except ZeroDivisionError:
                print("Rut incorrecto, ocurrio un error. Intentelo nuevamente.")             

        #------------------ Validar nombre ---------------------
        while True: 
            nombre=input("Ingrese su nombre y apellido.")
            contEspacios=0
            
            for i in nombre.strip():
                if i ==" ":
                    contEspacios+=1
            
            if  contEspacios==1:
                print("El nombre es correcto.")
                break      
            else:        
                print("El nombre es incorrecto.")    

        # ----------------- Validar edad -----------------------
        while True:
            edad=int(input("Ingrese edad."))
            if edad>=0 and edad<=130:
                print("Edad correcta.")
                break
            else:    
                print("Edad incorrecta.") 
                
        #------------------ Validar Email ----------------------
        while True:
            #---------- reset contador -------------
            contEsp=0
            contArroba=0
            correo=input("Ingresar correo.")
            correo2=correo.strip()
            
            for i in range(0,len(correo2)):
                if correo2[i]==" ":
                    contEsp+=1
                elif correo2[i]=="@":
                    contArroba+=1
                    
            if correo2[len(correo2)-1]=="@" or correo2[len(correo2)-1]=="." or correo2[0]=="@" or correo2[0]=="." or contEsp>0 or contArroba>1:
                print("El correo es incorrecto.")  
            else: 
                print("Correo correcto.")
                break
            
        #------------------ Validador de Genero ----------------
        while True:
            gen=input("Ingresar genero del cliente: \n(m: masculino - f: femenino - o: otros)").lower()
            if gen=="m" or gen=="f" or gen=="o":
                if gen=="m":
                    gen=="Masculino"
                elif gen=="f":
                    gen=="femenino"
                elif gen=="o":
                    gen=="otros"        
                print("Genero correcto "+gen.upper()+".")
                break
            else:
                print("Genero incorrecto.")
            
        #------------------ Estado suscripciones ------
        estadosSuscr="Suscrito el dia"
        
        datosCliente=f"Rut: {rut}\nNombre: {nombre}\nEdad: {edad}\nCorreo: {correo2}\n"

    if opc==2:
        while True:
            fechasuscr=input("Ingrese fecha de suscripcion")
            estadosSuscr+="Suscripcion el dia "+ fechasuscr
            break
            

        print(estadosSuscr)
       
    if opc==3:
        try:
            rutconsul=int(input("ingrese el rut del cliente."))
            if rutconsul==rut:
                print(datosCliente)
                print("registrado...")
            else:
                print("no registrado")         
        except NameError:
            print("No hay clientes registrados. Por favor registrar cliente antes de consultar.")       
                     
    if opc==4:
        print("Gracias por preferir Juan Maestro.")
        break    
