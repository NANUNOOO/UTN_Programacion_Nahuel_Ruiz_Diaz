numero = int(input("Ingrese un numero: "))

def verificar_par_impar(numero:int)->bool:
    if numero % 2 == 0:
        resultado = True
    else:
        resultado = False
    return resultado

print(verificar_par_impar(numero))