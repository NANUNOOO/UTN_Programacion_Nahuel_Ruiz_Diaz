from math import pi

def  calcular_area_circulo(radio):
    resultado = pi * radio ** 2
    return resultado


radio_usuario= float(input("ingrese el radio"))
variable = calcular_area_circulo()
print(variable)