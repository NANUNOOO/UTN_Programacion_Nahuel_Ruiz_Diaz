"""Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. Por defecto es del 1 al 10."""

def tabla_de_multiplicar(numero, inicio=1, fin=1)-> None:
    if inicio >= 1 and fin <=11:
        for i in range(inicio , fin + 1):
            print(f"El numero {numero} X {i} ) {numero * i}")
    else:
        print("ERROR parametro incorrecto...")
tabla_de_multiplicar(2,5,9)