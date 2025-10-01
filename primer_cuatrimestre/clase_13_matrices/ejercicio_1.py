"""
Crea un programa que encuentre el valor mas grande en una matriz de enteros.

Restricciones:

No uses listas por comprension, metodos de listas (como .max()), ni funciones integradas salvo len() y range().
usa unicamente bucles for y comparaciones directas.

Ejemplo: para la matriz
"""

matriz = [
    [5,3,2],
    [7,6,65],
    [22,63,8],
]

def valor_maximo(lista):
    maximo = float("-inf")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > maximo:
                maximo = matriz[i][j]
    return maximo

print(valor_maximo(matriz))