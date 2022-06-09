import random as rd

dinero_jug=10

while True:
    try:
        opc=int(input("Bienvenido al sistema de apuestas de dados\n------Menu------\n1. Apostar. \n2. Salir. "))
    except ValueError:
        print("ingresaste un valor erroneo, vuelve a intentarlo.")
        continue            
    if opc==1:
                if dinero_jug>0:
                    while True:
                        apuesta=int(input("¿Cuanto desea apostar?"))
                        if dinero_jug>=apuesta:
                            dinero_jug=dinero_jug-apuesta
                            dado1=rd.randint(1,6) #Tarea:Investigar la función uniform de la librería random
                            dado2=rd.randint(1,6)
                            print("Se han lanzado los dados.")
                            eleccion=int(input("Adivina, la suma de los dos numeros de los dados es par o impar.\n1.Par \n2.Impar\n"))
                            mod=(dado1+dado2)%2
                            if (eleccion==1 and mod==0) or (eleccion==2 and mod==1):
                                dinero_gan=apuesta*2
                                print(f"Acertaste, has ganado ${dinero_gan}.")
                                dinero_jug+=(dinero_gan)
                                print(dado1+dado2)
                            else:
                                print(f"Lo sentimos, has perdido ${dinero_jug}.")
                                print(dado1+dado2)
                            while True:
                                try:    
                                    opc2=int(input("¿Desea continuar apostando?\n1.Si 2.No"))
                                except:
                                    print("Has ingresado un valor no valido, intentelo nuevamente.")     
                                if opc2==1:
                                        break    
                                elif opc2==2:
                                        print(f"Su saldo final es de: ${dinero_jug}")
                                        break
                                else:
                                    print("opcion no valida intentelo nuevamente.")
                        
            
                        else:
                            print("Tiene que tener la cantidad apostada o mas, intetentelo nuevamente")
                        break                        
                else:
                    
                    print("Su saldo es 0 no puede seguir apostando.")
                    break            
    elif opc==2:                
                print("Hasta luego")
                print(f"Su saldo final es de: ${dinero_jug}")
                break
                            
    else:
                print("ingresaste una opcion incorrect, intentalo nuevamente")                   