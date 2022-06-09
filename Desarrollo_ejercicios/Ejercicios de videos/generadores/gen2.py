def devuelve_ciudades(*ciudades): #el * se agrega para decirle al generador que la cantidad de elementos que se ingresaran es indeterminada
    for elemento in ciudades:
        #for i in elemento:
             yield from elemento   
        
ciudades_devueltas=devuelve_ciudades("Concepción", "Viña del mar", "Valdivia", "Santiago") 

print(next(ciudades_devueltas))  

print(next(ciudades_devueltas)) 
     