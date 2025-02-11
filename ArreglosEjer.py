#Insertar
class Arreglo:
    def __init__(self):
        self.lista = []

    def Insertar(self):
        elemento = int(input("Inserta un Numero"))
        self.lista.append(elemento)

    def Mostrar(self):
        print(self.lista)

unalista = Arreglo()
unalista.Insertar()
unalista.Mostrar()

#Eliminar
class Lista:
    def __init__(self):
        self.arregloLista = [2,3,5]

    def Eliminar(self,Indice):
        if 0 <= Indice < len(self.arregloLista):
            self.arregloLista.pop(Indice)
            print(f"El nuevo arreglo es {self.arregloLista}")
        else:
            print("indice inexistente")

lista = Lista()
Indice = int(input("Ingrese el indice a remover: "))
lista.Eliminar(Indice)

#Modificar
class Arreglos:
    def __init__(self):
        self.arregloList = [10, 20, 30, 40]

    def modificar(self,index):
        Lugar = int(input("Lugar a cambio"))
        if 0<= index < len(self.arregloList):
            nuevoValor = int(input("Escribar el nuevo valor"))
            self.arreglolist[index] = nuevoValor
            print(f"Nuevo arreglo: {self.arregloList}")
        else:
            print("Índice fuera de rango")

arreglo = Arreglos()
indice = int(input("Ingrese el índice a modificar: "))
arreglo.modificar(indice)

