class Coche():
    #caracteristicas de la clase
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enMarcha=False
    
    #Comportamientos del coche
    #Crear metodo.
    def arrancar(self):
      self.enMarcha=True  
 
    
    def estadoCoche(self):
        if (self.enMarcha):
            return "El coche está en marcha."
        else:
            return "El coche está detenido."
  
#instanciar una clase.  
miCoche=Coche()

print(f"El largo del coche es: {miCoche.largoChasis}")
print(f"El ancho del coche es: {miCoche.anchoChasis}")
print(f"El coche tiene: {miCoche.ruedas}")
# Con el metodo arrancar se pone en marcha el coche.
miCoche.arrancar()
print(miCoche.estadoCoche())   