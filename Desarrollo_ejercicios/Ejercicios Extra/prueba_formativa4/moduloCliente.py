class Cliente():
    
    def __init__(self, rut, nombre, celular, banco):
        self.rut=rut
        self.nombre=nombre
        self.celular=celular
        self.banco=banco
        
    def mostrarDatos(self):
        print(f"----------- Datos del cliente -----------\nRut: {self.rut}\nNombre: {self.nombre}\nCelular: {self.celular}\n Banco: {self.banco}\n---------------------------------------")    
 