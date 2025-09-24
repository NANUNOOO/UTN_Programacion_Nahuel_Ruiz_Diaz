"""
Agregar
Nombre de la función:
agregar(lista, elemento)

Objetivo:
Agregar un elemento al final de la lista.

Tarea:
Modificar la lista original, añadiendo elemento como su último elemento.
No es necesario retornar un valor (solo modificar la lista) """
lista = [1, 2, 3]
elemento = ""
def agregar(lista: list, elemento: int)-> list:
    elemento = int(input("Ingrese el elemnto a agregar: "))
    lista = lista + [elemento]
    return lista
print(lista)
print(agregar(lista, elemento))