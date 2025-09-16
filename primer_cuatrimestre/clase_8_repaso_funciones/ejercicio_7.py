"""Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario."""

numero = int(input("Ingrese un numero: "))

def verificar_par_impar(numero:int)->bool:
    if numero % 2 == 0:
        resultado = True
    else:
        resultado = False
    return resultado

print(verificar_par_impar(numero))