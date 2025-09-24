# Crea una funcion suma_positivos(lista) que se le pase una lista y sume los elementos positivos.
# si se le pasa un parametro que no es una lista debera retornar un mensaje advirtiendo tal caso.

lista = "hola"

def suma_positivos(lista):
    suma = 0
    if type (lista) == list:
        for i in range(len(lista)):
            if lista[i] >= 0:
                suma += lista[i]
                mensaje = f"La suma de los elementos positivos es: {suma}"
    else:
        mensaje = f"ERROR, ingrese una lista..."
    
    return mensaje



print(suma_positivos(lista))