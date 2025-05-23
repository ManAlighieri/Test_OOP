import json
import requests

class GestorJson:
    def __init__(self,arch):
        self.arch = arch
    
    def leerJson(self):
        try:
            with open(self.arch, 'r') as f:
                return json.load(f)
            
        except FileNotFoundError:
            print("Archivo no existe")
            return {}
        except json.JSONDecodeError:
            print("El archivo no es json")
            return {}
        
    def escribirJson(self,datos):
        with open(self.arch, 'w') as f:
            return json.dump(datos,f, indent= 4)
    
    def modificarjson(self,llave,valor):
        datos = self.leerJson()
        datos[llave] = valor
        self.escribirJson(datos)

    def obtenerPokemon(self,pokemon):
        try:
            url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
            response =requests.get(url)
            response.raise_for_status()
            data=response.json()
            self.escribirJson(data)
        except requests.exceptions.HTTPError:
            print("El enlace no existe")
        except requests.exceptions.RequestException:
            print("No se pudo realizar la peticion")

gjson = GestorJson("pokemon.json")
gjson.obtenerPokemon("pikachu")
PokemonInfo = gjson.leerJson()
print(PokemonInfo)

habilidades = PokemonInfo["abilities"]
print("Habilidades:")
for habilidad in habilidades:
    print(habilidad["ability"]["name"])



