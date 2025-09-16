"""Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario."""

def primo_o_compuesto(numero):
    estado = True
    if numero < 2: 
        return "error"
    for i in range(2,numero):
        estado = False
        break
    return estado
valor_numero = int(input ("ingrese un numero"))
resultado = primo_o_compuesto(valor_numero)
print(resultado)