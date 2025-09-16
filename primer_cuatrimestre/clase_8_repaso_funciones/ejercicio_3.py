
"""Crear una función que le solicite al usuario el ingreso de una cadena y la retorne."""


def retorno_cadena():

    cadena = input("Introduzca un valor string: ")
    while len(cadena) <= 4 and len(cadena) >= 10:
        cadena = input("Introduzca un valor string: ")
        
    return cadena

print(retorno_cadena())