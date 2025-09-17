# Definir una funcion que reciba como parametro un str y devuelva la cantidad de LETRAS que contiene dicha cadena.


# Pista: if ingreso[i] >= "a" and ingreso[i] <= "Z"

#EJ: contar_letras("hola mundo") -> 9 letras
#EJ: contar_letras("hola        mundo") -> 9 letras
#EJ: contar_letras("hola   124    mundo") -> 9 letras

def contar_letras():
    contador_letras = 0
    ingreso = input("Ingrese una cadena: ")
    for i in range(len(ingreso)):
        if ingreso[i] >= "a" and ingreso[i] <= "z":
            contador_letras += 1
        elif ingreso[i] >= "A" and ingreso[i] <= "Z":
            contador_letras += 1
    return contador_letras

contador = contar_letras()
print("La cantidad de letras es: ", contador)