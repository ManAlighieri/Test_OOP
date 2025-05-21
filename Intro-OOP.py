class cuadrado:
    def perimetro(self,lado):
        return 4 * lado
    def area(self,lado):
        return lado * lado 
Cuadrado = cuadrado()
lado = 5
P=Cuadrado.perimetro(lado)
A=Cuadrado.area(lado)
print(f"Perímetro del cuadrado: {P}")
print(f"Área del cuadrado: {A}")