"""
desarrollar una funcion que reciba por parametro una matriz (lista de listas de numeros) y un numero especificado. 
la funcion debe buscar el numero en toda la matriz y retornar true si existe. 
si no existe, retornar false.
"""

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

def encontrar_numero(matriz,numero):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                return True
    return False

print(encontrar_numero(matriz,2))