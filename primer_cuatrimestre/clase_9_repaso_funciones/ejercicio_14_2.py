# Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 

# Validaciones a realizar: 
# Que el valor retornado no sea un a cadena vacía -> ""
# Que el valor retornado no sea una cadena con solo espacios -> "  "

def validar_ingreso_cadena()-> str:
    ingreso_valido = False
    ingreso = input("Ingrese una cadena: ")
    while not ingreso_valido:
        contador_espacios = 0
        if ingreso == "": 
            ingreso = input("Ingreso invalido. Ingrese una cadena: ")
        else:
            for i in range(len(ingreso)):
                if ingreso[i] == " ":
                    contador_espacios += 1
            if contador_espacios == len(ingreso):
                ingreso = input("Ingreso invalido. Ingrese una cadena: ")
            else: 
                ingreso_valido = True
    return ingreso

ingreso_validado = validar_ingreso_cadena()
print("Ingreso validado: ", ingreso_validado)