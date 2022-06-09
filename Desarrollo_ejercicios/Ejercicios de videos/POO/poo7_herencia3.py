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
    
    
class Moto(Vehiculo):
    hcaballito=""
    def caballito(self):
        self.hcaballito="Voy haciendo caballito."
    def estado(self):   
        print(f"Marca: {self.marca} \nModelo: {self.modelo}\nEn marcha: {self.enmarcha}\nAcelerando: {self.acelera}\nFrenando: {self.frena}\n{self.hcaballito}")  

class Furgoneta(Vehiculo):
    
    def carga(self, cargar):
        self.cargado=cargar
        if (self.cargado):
            return "La furgoneta está cargada."
        else:
            return "La furgonate no está cargada."    


class VElectrico(Vehiculo):
    
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia=100
        self.cargando=False
        
    def cargarEnergia(self):
        self.cargando=True    
     
    def estado(self):
        super().estado()
        print(f"Autonomia: {self.autonomia} hrs.\nCargando: {self.cargando}")    

miFurgoneta=Furgoneta("Renault", "Kangoo")

miFurgoneta.arrancar()

miFurgoneta.estado()

print(miFurgoneta.carga(True))

print("....................")

miMoto=Moto("Honda", "CBR")

miMoto.caballito()

miMoto.estado() 

print("....................")    

class BicicletaElectrica(VElectrico):
    pass

miBici=BicicletaElectrica("Trek","Marlin 5")

miBici.estado()