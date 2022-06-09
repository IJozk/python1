while True:
    gen=input("Ingresar genero del cliente: \n(m: masculino - f: femenino - o: otros)").lower()
    if gen=="m" or gen=="f" or gen=="o":
                if gen=="m":
                    gen="Masculino"
                elif gen=="f":
                    gen="femenino"
                elif gen=="o":
                    gen="otros"        
                print("Genero correcto. "+gen.upper())
                break
    else:
                print("Genero incorrecto.")