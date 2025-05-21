#Diccionarios
Dic = {"x": "equis", "y": "ye", "D": "De"}
print(Dic['x'])               
print(Dic.get('x'))           
print(Dic.get('z'))          

Dic['x'] = "equisD"
Dic['z'] = "Zeta"
del Dic['y']


X = Dic.pop('y', "No existe")
print(X)                     

print('x' in Dic)            
print(Dic.keys())            
print(Dic.items())           
Dic.clear()
Dic.update({'x': "x"})

print(Dic.get('x', "equis")) 
