class Pisto:
    def __init__(self,hielera,hielera2):
        self.__hielera = hielera
        self.hielera2 = hielera2
    
    def pistear1(self):
        self.__hielera = "vaciar"
        return self.__hielera
    
    def pistear2(self):
        self.hielera2 = "Nah, esta vacia"
        return self.hielera2
Fiesta = Pisto ("Carton en hielera","Unas cuantas frias")
print(Fiesta.pistear1())
print(Fiesta.pistear2)

