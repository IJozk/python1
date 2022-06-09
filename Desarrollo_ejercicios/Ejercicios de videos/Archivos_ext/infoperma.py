import pickle

class Persona():
    
    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se a creado una persona una nueva persona con el nombre de ", self.nombre)
        
    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class listaPersonas():
    
    personas=[]
    
    def __init__(self):
        
        listaDePersonas=open("ficheroExterno", "ab+")
        listaDePersonas.seek(0)
        
        try:
            self.personas=pickle.load(listaDePersonas)
            print("Se cargaron {} personas del fichero externo.".format(len(self.personas)))
        except:
            print("El fichero esta vacio.")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)        
            
    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()
        
    
    def mostrarPersonas(self):
        for p in self.personas:
            print(p)
            
    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas=open("ficheroExterno", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close() 
        del(listaDePersonas)
        
    def mostrarInfoFicheroExterno(self):
        print("La informacion del fichero externo es la siguiente.")
        for p in self.personas:
            print(p)               

miLista=listaPersonas()
p=Persona("Sandra", "fem", 30)
miLista.agregarPersonas(p)


miLista.mostrarInfoFicheroExterno() 
    


        