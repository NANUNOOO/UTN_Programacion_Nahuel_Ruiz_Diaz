"""Mostrar la suma de los números pares desde el 1 hasta el 10."""

numero = 1
suma = 0
while numero <= 10:
    if numero % 2 == 0:
        suma = suma + numero
        print (suma)
    numero += 1