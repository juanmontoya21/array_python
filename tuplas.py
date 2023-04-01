#tuplas: son inmutables(no se pueden modificar; no se pueden eliminar elementos)
#metodos que no se pueden usarse en las tuplas: append(), remove(),insert(), clear(),pop()

tuplas=() #tupla vacia

tupla= 1,2,3,4,5

print(type(tuplas))
print(type(tupla))

tupla2=1,
tupla3=3

print(type(tupla2))
print(type(tupla3))

elemento = tupla[2]

print(elemento)

for i in tupla:
    print(i)

for j in range(len(tupla)):
    print(tupla[j])

#index()
posicion =tupla.index(3)
print(posicion)


#listasa: sort() organizar de forma ascendente, sort(reverse=true) organizar de forma descendente, count() contar datos repetidos

numeros = [3,34,5,70,1,4,6,6]

numeros.sort()
print(numeros)

desc = numeros.sort(reverse=True)

print(numeros)

contar = numeros.count(6)

print(contar)