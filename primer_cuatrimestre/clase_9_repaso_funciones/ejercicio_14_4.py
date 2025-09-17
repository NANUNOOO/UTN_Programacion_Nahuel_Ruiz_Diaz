# Definir una función que reciba como parámetro un str y devuelva la cantidad de PALABRAS que contiene dicha cadena.

# EJ: contar_palabras("Hola mundo") -> 2 palabras 
# EJ: contar_palabras("Hola              mundo  ") -> 2 palabras
# EJ: contar_palabras("Hola    124          mundo  ") -> 3 palabras
# EJ: contar_palabras("Hola    124          mundo  ") -> 2 palabras

def validar_caracter_alfabetico(caracter: str)-> bool:
    if (caracter >= "a" and caracter <="z") or (caracter >= "A" and caracter<="Z"):
        return True
    return False

def contar_palabras(mensaje:str) -> int:
    contador_palabras = 0
    dentro_de_palabra = False
    for i in range(len(mensaje)):
        if mensaje[i] != " " and not dentro_de_palabra:
            dentro_de_palabra = True
            contador_palabras += 1
        elif mensaje[i] == " ":
            dentro_de_palabra = False
    return contador_palabras

print(contar_palabras(""))