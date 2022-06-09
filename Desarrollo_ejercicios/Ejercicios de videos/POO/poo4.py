class Coche():
    #caracteristicas de la clase
    #Estado inicial:
    def __init__(self):
        
        #Para encapsular una variable hay que escribir __ antes del nombre de la variable en el constructor de la clase.
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enMarcha=False
    
    #Comportamientos del coche
    #Crear metodo.
    def arrancar(self,arrancamos):
        self.__enMarcha=arrancamos
        
        if(self.__enMarcha):
            chequeo=self.__chequeo_interno()
        
        if(self.__enMarcha and chequeo):
            return "el coche está en marcha."
        
        elif(self.__enMarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo, no se puede arrancar."
        
        else:
            return "el coche está detenido."
 
    
    def estadoCoche(self):
        return f"El coche tiene {self.__ruedas} ruedas, un ancho de {self.__anchoChasis} metros y un largo de {self.__largoChasis}"
    
    # Metodo encapsulado.
    def __chequeo_interno(self):
        print("Realizando chequeo interno.")
        
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"
        
        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False
       
  
#instanciar una clase.  
miCoche=Coche()

print(f"{miCoche.estadoCoche()}. Además {miCoche.arrancar(True)}")  

print("------------A continuacion creamos un segungo objeto.------------")

miCoche2=Coche()

print(f"{miCoche2.estadoCoche()}. Además {miCoche2.arrancar(False)}")  