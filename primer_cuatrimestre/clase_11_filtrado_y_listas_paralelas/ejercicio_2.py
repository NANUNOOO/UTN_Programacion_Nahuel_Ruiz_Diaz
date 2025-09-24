""" 
Insertar

Nombre de la función:
insertar(lista, elemento, indice)

Objetivo:
Insertar un elemento en una posición específica de la lista.

Tarea:
Modificar la lista original, colocando elemento en la posición indicada por indice.
Si el índice es mayor al tamaño de la lista, el elemento se agrega al final.
Ejemplo: Si la lista es [10, 20, 30] y se inserta 5 en el índice 1, la lista resultante será [10, 5, 20, 30].
"""
lista = [10, 20, 30]
print(lista)

def insertar(lista, elemento, indice):
    if indice >= len(lista):
        lista = lista + [elemento]
    else:
        lista[indice:indice] = [elemento] 
    print(lista)

insertar(lista, 777, 70)
