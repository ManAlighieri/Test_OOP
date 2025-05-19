#Diccionarios
Dic={"x":"equis","y":"ye","D":"De"}
Dic2=dict(x="equis",y="ye",D="DC")
print(Dic['x'])
print(Dic.get('x'))
print(Dic.get('z'))
Dic['x']="equisD"
Dic['z']="Zeta"
del Dic['y']
X = Dic.pop('y')
print(X)
print('x' in Dic)
llaves = Dic.keys()
print(llaves)
Valores = Dic.values()
P=Dic.items()

Dic.clear()
Dic.update({x:"x"})
Dic.get('x',"equis")
