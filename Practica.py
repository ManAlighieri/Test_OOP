class Figura:
    def area(Lados, Medidalados):
        if Lados == 4:
            print("Es un cuadrado")
            Area = Medidalados * Medidalados
            print("El Area es:", Area)
        elif Lados == 3:
            print("Es un triangulo")
    
    def perimetro(Lados, Medidalados):
        if Lados == 4:
            perimetro = Medidalados * 4
            print("El perimetro es:", perimetro)

Figura.area(4, 5)
Figura.perimetro(4, 5)

