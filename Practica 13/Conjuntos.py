A = {1,2,3}
B = {3,4,5}
#Union
U = B.union(A)
print(U)
U = A|B
#Interseccion
I = B.intersection(A)
print(I)
I = A&B
#Diferencia
D = A.difference(B)
print(D)
D=A-B
#Diferencia Simetrica
DS = A.symmetric_difference(B)
print(DS)
DS = A^B

A.issubset(B)
B.issuperset(A)

C={}
print(type(C))
C=set()

Ac = len(A)
A.clear()
E=A.copy()
A.isdisjoint(B)