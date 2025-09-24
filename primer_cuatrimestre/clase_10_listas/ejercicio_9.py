# Ejercicio de busqueda y remplazo. a partir de la siguiente lista:
# lista = [1, 2, 3, 4, 2, 5, 2]
# Nos solicitaron que remplacemos los numeros 2 por los numeros 9

lista = [1, 2, 3, 4, 2, 5, 2]
print(lista)

def remplazo_numero(lista):
    for i in range(len(lista)):
        if lista[i] == 2:
            lista[i] = 9
    return lista

print(remplazo_numero(lista))
