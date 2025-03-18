class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"
# Crear un objeto
juan = Persona("Juan", 30)
print(juan.saludar()) # Output: Hola, soy Juan y tengo 30 años