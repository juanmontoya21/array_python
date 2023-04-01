diccionarios = {} #diccionarios vacio

diccionario1 = dict()
print(type(diccionario1))
print(type(diccionarios))

dicc = {
    "nombre": "juan",
    "edad": 18,
    "sexo": "M",
    "F_Ncto": "21/05/2004"
}

print(dicc["nombre"])

datos1 =dict(
    Nombre = "juan",
    Edad = 18,
    Sexo = "M",
    F_Ncto = "21/05/2004")

print(datos1["F_Ncto"])

datos1["Nombre"]="sebastian"
datos1["Sexo"]="F"
datos1["direccion"]="calle siempre viva"

print(datos1)

#METODOS GET() devuelve el elemento de la clave 
print(datos1.get("Edad"))

#Metodo Update(): actualizar el diccionario

animales = {
    "invertebrado": "gusano", "Vertebrados": "elefante",
    "carnivoro": "leon", "omnivoro": "Raton"
}

marcas = {
    "Tenis": "Nike","celular": "Nokia","carro": "mazda",
    "colchones": "comodisimos"
}

animales.update(marcas)

print(animales)

print(marcas)

#Metodos pop(). eliminar la clave pasada como argumento y su valor

animales.pop("Vertebrados")

print(animales)

#imprimir solo claves del diccionario

print(animales.keys())

for clave in animales.keys():
    print(clave)

#imprimir solo los  valores 
print(animales.values())

for valor in animales.values():
    print(valor)

#imprimir: clave y valor

print(animales.items())

for clave, valor in animales.items():
    print(clave, "->", valor)

#eliminar todos los elementos del diccionario

animales.clear()

print(animales)
