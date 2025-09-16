"""Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar."""

numero = int(input("Ingrese un numero: "))

def verificar_par_impar(numero:int)->None:
    if numero % 2 == 0:
        print("su numero es par...")
    else:
        print("su numero es impar...")

verificar_par_impar(numero)