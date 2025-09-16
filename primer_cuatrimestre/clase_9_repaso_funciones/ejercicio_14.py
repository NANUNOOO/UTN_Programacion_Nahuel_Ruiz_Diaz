""" """

def validar_ingreso_numerico(ingreso:str)->str:
    ingreso_valido = False
    ingreso = input("Ingrese un numero")
    
    while not ingreso_valido:
        ingreso_a_castear = ""
        for i in range(len(ingreso)):
            match ingreso[i]:
                case "0"|"1"|"2"|"3"|"4"|"5"|"6"|"7"|"8"|"9":
                    ingreso_a_castear += ingreso[i]
                    ingreso_valido = True
                case _:
                    print("Ingreso invalido")
                    ingreso = input("Ingrese un numero: ")
                    ingreso_valido = False
                    break
    return int(ingreso)

ingreso_validado = validar_ingreso_numerico()
print("Ingreso validado: ", ingreso_validado)