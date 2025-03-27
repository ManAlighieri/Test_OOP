#Encapsulamiento
class Cliente:
    def __init__(self):
        self.__codigo = 5
    
    def __cuenta(self):
        print("Cuenta de procesamiento")

    def get_codigo(self):
        return self.__codigo


persona = Cliente()
print(persona.get_codigo())

#Herencia
class Animal:
    def __init__(self,nombre):
        self.nombre = nombre

    def hacerSonido(self):
        return "Sonido Generico"

class Perro(Animal):
    def hacerSonido(self):
        return "guau guau"

Perrito=Perro("Firulais")
print(Perrito.nombre)
print(Perrito.hacerSonido())
