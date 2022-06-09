class Cliente():
    
    def __init__(self, rut, nombre, direccion, comuna, correo, edad, genero, celular, tipo):
        self.rut=rut
        self.nombre=nombre
        self.direccion=direccion
        self.comuna=comuna
        self.correo=correo
        self.edad=edad
        self.genero=genero
        self.celular=celular
        self.tipo=tipo
        self.suscripcion=(("suscrito","00/00/00"),)
        
    def mostrarDatos(self):
        print(f"----------- Datos del cliente -----------\nRut: {self.rut}\nNombre: {self.nombre}\nDireccion: {self.direccion}\nComuna: {self.comuna}\nCorreo: {self.correo}\nEdad: {self.edad}\nGenero: {self.genero}\nCelular: {self.celular}\nTipo: {self.tipo}\nCliente {self.suscripcion[len(self.suscripcion)-1][0]} el dia {self.suscripcion[len(self.suscripcion)-1][1]}\n---------------------------------------")    
 