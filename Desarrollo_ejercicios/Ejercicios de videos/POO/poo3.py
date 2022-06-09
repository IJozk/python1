class Coche():
    #caracteristicas de la clase
    #Estado inicial:
    def __init__(self):
        
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enMarcha=False
    
    #Comportamientos del coche
    #Crear metodo.
    def arrancar(self,arrancamos):
        self.__enMarcha=arrancamos
        if(self.__enMarcha):
            return "el coche está en marcha."
        else:
            return "el coche está detenido."
 
    
    def estadoCoche(self):
        return f"El coche tiene {self.__ruedas} ruedas, un ancho de {self.__anchoChasis} metros y un largo de {self.__largoChasis}"
       
  
#instanciar una clase.  
miCoche=Coche()

print(f"{miCoche.estadoCoche()}. Además {miCoche.arrancar(True)}")  

print("------------A continuacion creamos un segungo objeto.------------")

miCoche2=Coche()
#Lo sig no deberia permitirse. Al ingresar en el atributo ruedas un valor diferente este cambiara y la idea es que  esto no ocurra. Para ello habrá que encapsular las variables.
#Para ello hay que escribir __ antes del nombre de la variable en el constructor de la clase.
miCoche2.__ruedas=2

print(f"{miCoche2.estadoCoche()}. Además {miCoche2.arrancar(False)}")  