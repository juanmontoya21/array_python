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