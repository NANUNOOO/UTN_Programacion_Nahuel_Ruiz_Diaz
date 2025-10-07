# Crear una funcion llamada ordenar_array que reciba como parametro n array de numeros enteros y 
# lo ordene de forma ascentdente. la funcion debe implementar como algoritmo de ordenamiento el
# metodo de la burbuja. ademas,como parametro opcional debe recibir un booleano (quepor default esta en False),
# que en caso de ser True ordena el vector en forma decendente.

lista = [3,2,5,4,1]

def ordenar_array(lista, decendente=False):
    n = len(lista)
    for i in range(n-1):
        for j in range(n-1):
            if decendente == False and lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
            
            elif decendente == True:
                if lista[j] < lista[j+1]:
                    aux = lista[j]
                    lista[j] = lista[j+1]
                    lista[j+1] = aux
    return lista

print(ordenar_array(lista,True))





