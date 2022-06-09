class Vehiculo():
    
    def __init__(self, marca, modelo):
        
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
    
    def arrancar(self):
        
        self.enmarcha=True
        
    def acelerar(self):
        
        self.acelera=True
        
    def frenar(self):
        
        self.frena=True
        
    def estado(self):
        
        print(f"Marca: {self.marca} \nModelo: {self.modelo}\nEn marcha: {self.enmarcha}\nAcelerando: {self.acelera}\nFrenando: {self.frena}") 
    
#Asi la clase Moto hereda todas las caracteristicas y comportamioentos de la superclase vehiculo.    
class Moto(Vehiculo):
    pass

#Al crear una instancia de Moto debemos ingresar los parametros que nos pide el constructor de vehiculo.
miMoto=Moto("Honda", "CBR")

miMoto.estado()                       