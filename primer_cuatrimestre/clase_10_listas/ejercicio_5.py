# De estas edades 34, 54, 12, 76, 2, 9, 34, 87 nos solicitan que:

# Guardemos en una variable la mas alta y en otra la mas baja.
# Y despues mostremos por pantalla.


lista = [34, 54, 12, 76, 2, 9, 34, 87]

def edad_mas_alta(lista:list)->int:
    num_max = float('-inf')
    for i in range(len(lista)):
        if lista[i] > num_max:
            num_max = lista[i]
    return num_max


def edad_mas_baja(lista:list)->int:
    num_min = float('inf')
    for i in range(len(lista)):
        if lista[i] < num_min:
            num_min = lista[i]
    return num_min

print(edad_mas_alta(lista))
print(edad_mas_baja(lista))