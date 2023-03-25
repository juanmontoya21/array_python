#Listas
Lista1=[] #lista vacia
Lista1 = [1, "hola", 1.25,True,False] #lista con diferentes tipos de datos

texto = "Hola Mundo" #las cadenas de texto tambien son listas

#mutable: modificar ,  eliminar, extender, actualizar
#indexada: el primer dato esta en la posicion 0
#len: longitud de la lista o array
longitud = len(Lista1)

print(f"cantidad de elementos: {longitud}")

#AGREGAR ELEMNETOS A LA LISTA append()
Lista1.append("colecciones")
print(Lista1)
#insertar un elemento con un indice que usted quiera
insertar_elemento= Lista1.insert(2, 4)

#acceder a un elemento de la lista
elemento = Lista1[-2]
print(elemento)

#eliminar un elemento: pop(), remove(elemento)
borrar= Lista1.pop(1) 

print(Lista1)

eliminar = Lista1.remove("colecciones")
print(Lista1)

#conocer el indice o posicion del elemento: index(elemento)
Lista1 = [1, 4, 1.25, True, False, 'colecciones']
posicion= Lista1.index(False)

print(posicion)

animales = ["Perro","gato","Caballo","Tortuga"]
animales_acuaticos = ["delfin","ballena","tiburon"]

animales.extend(animales_acuaticos)

print(animales)

#eliminar todos los elementos de una lista: clear()
animales.clear()

print(animales)

#recorrer una lista 

lenguajes_PR = ["Python", "Html", "Css", "C++"]

for e in lenguajes_PR:
    print(e)

#recorrer teniendo en cuenta la posicion 
for indice in range(len(lenguajes_PR)):
    print(lenguajes_PR[indice],"esta en la posicion", indice)

par = []
impar = []

numero1= int(input("ingrese el primer numero: "))
numero2=int(input("ingrese el numero que determine el rango: "))

"""for indice in range(numero1,numero2):
    if indice % 2 ==0:
        par.append(indice)
    else :
        impar.append(indice)

print(par)
print(impar)"""

while numero1 <= numero2 :
    numero1+=1
    if numero1 % 2 == 0:
        par.append(numero1)
    else:
        impar.append(numero1)

print(par)
print(impar)
