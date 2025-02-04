import math

class Figura:
    def Poly(Lados,nLados):
        if nLados > 4: 
            P = Lados * nLados
            A = (nLados * Lados**2) / (4 * math.tan(math.pi / nLados))
        else:
            P = None
            A = None
        return P, A

# Get user input
nLados = int(input("Ingrese el número de lados: "))
Lados = float(input("Ingrese el tamaño de los lados: "))

# Calculate perimeter and area
perimetro, area = Figura.Poly(Lados, nLados)

print(f"Perímetro: {perimetro}")
print(f"Area: {area}")