# Nos solicitaron que filtremos los numeros pares de la siguiente lista:
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [None] * len(lista)
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        lista2[i] = lista[i]

print(lista2)