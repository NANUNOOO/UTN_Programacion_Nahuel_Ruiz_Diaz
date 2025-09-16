numero = int(input("Ingrese un numero: "))

def verificar_par_impar(numero:int)->None:
    if numero % 2 == 0:
        print("su numero es par...")
    else:
        print("su numero es impar...")

verificar_par_impar(numero)