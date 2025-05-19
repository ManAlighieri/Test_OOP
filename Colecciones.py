import numpy as np

lista1 = [1,1.1,3,"Pepe","Serch"]
lista2 = np.array([1,2,3,4,5])

tupla1 = tuple(lista1)
conj1 = set(lista1)

tupla2 = tuple(lista2)
conj2 = set(lista2)

lista1.append(5)
lista1.insert(1,"Hola")
lista1.extend([2,"Hola2"])
lista1.index(1)
lista1.count(1)
x = 1 in lista1


diccionario = {"1":1,
               "2":True,
               "3": 3.3,
               "4": "4",
               "5":{1}}
print(tupla2)

