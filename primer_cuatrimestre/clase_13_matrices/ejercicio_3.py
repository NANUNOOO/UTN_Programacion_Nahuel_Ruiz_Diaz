"""
Desarrollar una funcion que reciba una matriz (lista de listas de numeros) y un numero especificado.
la funcion debe buscar el numero en toda la matriz y retornar una lista con todas las posiciones donde se encuentra 
(como lista de fila y columna).
si el numero no se encuentra en la matriz, imprimir el mensaje "El numero no se encuentra en la matriz"
"""

matriz = [
    [1,2,3],
    [2,5,6],
    [7,8,2],
]

def encontrar_numero(matriz,numero):
    posiciones = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                posiciones += [[i,j]]
    if posiciones != []:
        return posiciones
    else:
        return "El numero no se encuentra en la matriz"


print(encontrar_numero(matriz,2))