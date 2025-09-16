from math import pi

"""Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área."""

def  calcular_area_circulo(radio):
    resultado = pi * radio ** 2
    return resultado


radio_usuario = float(input("ingrese el radio"))
variable = calcular_area_circulo()
print(variable)