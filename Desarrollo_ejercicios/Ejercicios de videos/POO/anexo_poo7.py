class Persona():
    
    def __init__(self, nombre, edad, domicilio):
        self.nombre=nombre
        self.edad=edad
        self.domicilio=domicilio
        
    def descripcion(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nDomicilio: {self.domicilio}")    
        
class Empleado(Persona):
    
    def __init__(self, salario, antiguedad, nombre_emp, edad_emp, domicilio_emp):
        super().__init__(nombre_emp, edad_emp, domicilio_emp)
        self.salario=salario
        self.antiguedad=antiguedad  
        
    def descripcion(self):   
        super().descripcion()
        print(f"Salario: {self.salario}\nAntigûedad: {self.antiguedad}")
                  
        
Antonio=Empleado(2000, 30, "Antonio", 44, "Chile")   

Antonio.descripcion()   

print(isinstance(Antonio, Persona))  