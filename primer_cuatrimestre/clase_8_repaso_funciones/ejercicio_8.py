"""Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande."""

def numero_maximo(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num3:
        return num3
    else:
        return num3


print(numero_maximo(58,18,6))