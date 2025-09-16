# Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.

# Validaciones a realizar: 
# Que el programa no rompa al ingresar un valor no numerico
# Que el ingreso contenga un '.' cómo máximo

def validar_ingreso_flotante()-> float:
    ingreso_valido = False
    ingreso = input("Ingrese un número: ")
    while not ingreso_valido:
        contador_comas = 0
        primer_vuelta = True
        for i in range(len(ingreso)):
            match ingreso[i]:
                case "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9":
                    ingreso_valido = True
                case "-": 
                    if not primer_vuelta:
                        print("Ingreso invalido.")
                        ingreso = input("Ingrese un número: ")
                        ingreso_valido = False
                        break
                case ".":
                    contador_comas += 1
                    if contador_comas > 1:
                        print("Ingreso invalido.")
                        ingreso = input("Ingrese un número: ")
                        ingreso_valido = False
                        break
                case _:
                    print("Ingreso invalido.")
                    ingreso = input("Ingrese un número: ")
                    ingreso_valido = False
                    break
            if primer_vuelta:
                primer_vuelta = False
    return float(ingreso)

ingreso_validado = validar_ingreso_flotante()
print("Ingreso validado: ", ingreso_validado)