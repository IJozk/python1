''' Un juego consiste en el lanzamiento de dos dados. Los jugadores
    deben adivinar si la suma de los dos dados es par o impar.
    Simule el juego en Python donde un jugador deberá ingresar cuánto
    dinero desea apostar en cada turno(Asuma que el jugador comienza con $10
    en su billetera.
    - Si adivina : Gana el total que apostó.
    - Si no adivina : Pierde lo que aposto.
    El juego termina cuando el usuario se queda sin dinero o ingrese que no
    desea continuar.
    Se deberá mostrar el resultado de cada ronda, el dinero que tiene en la
    billetera y al finalizar todas las rondas se deberá mostrar la cantidad
    de partidas que ganó el jugador. Utilice la función random para generar los
    números del dado.
'''

import random as rd    
print("Bienvenido al Juego de Dados")
print("Usted tine $10 para jugar ")
billetera = 10
cont_gana = 0 #Contador de las veces que ha ganado en cada partida
continuar="si"
while billetera > 0 and continuar == 'si':
    apuesta=int(input("Ingrese cantidad de $ a apostar ==>"))
    if apuesta <= billetera:
        dado1=rd.randint(1,6) #Tarea:Investigar la función uniform de la librería random
        dado2=rd.randint(1,6)
        total=dado1 + dado2
        resto=total % 2
        parimpar=input("Adivina si la suma de los dados es par o impar ? ==> ")
        print("El resultado fue: {} + {} = {}".format(dado1,dado2,total))
        if resto==0 and parimpar=='par':
            print("Felicitaciones Ganaste !!")
            billetera+=apuesta
            cont_gana+=1
        elif resto!=0 and parimpar=='impar':
            print("Felicitaciones Ganaste !!")
            billetera+=apuesta
            cont_gana+=1
        else:
            billetera-=apuesta
            print("Lamentablemente has Perdido !!")
        print("Lo que le queda en la Billetera es :",billetera)
        if billetera != 0:
            continuar=input("Desea seguir jugando si/no ==> ") 
            print(" ----------------------------------")
                    
    else:
        print("La apuesta es mayor al dinero que tienes en la billetera :( ")

print("Usted ha ganado {} partidas".format(cont_gana))
print("Gracias por haber Jugado ")





