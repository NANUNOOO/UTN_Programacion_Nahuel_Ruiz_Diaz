def retorno_cadena():

    cadena = input("Introduzca un valor string: ")
    while len(cadena) <= 4 and len(cadena) >= 10:
        cadena = input("Introduzca un valor string: ")
        
    return cadena

print(retorno_cadena())