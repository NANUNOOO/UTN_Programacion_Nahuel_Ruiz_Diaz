def cargar_vuelos(vuelos: list) -> list:
    cantidad = int(input("\n¿Cuantos vuelos quiere ingresar?: "))
    while cantidad > 100:
        cantidad = int(input("\nERROR, Cantidad maxima de cien: "))
    for i in range(cantidad):
        codigo = input("\nIngrese el codigo del vuelo: ")
        codigo = validar_ingreso_codigo_vuelo(codigo)
        destino = input("\nIngrese el destino del vuelo: ")
        precio = int(input("\nIngrese el precio del vuelo: "))
        vuelos += [[codigo, destino, precio]]
    return vuelos


def validar_ingreso_codigo_vuelo(codigo: str) -> str:
    ingreso_valido = False

    while not ingreso_valido:
        for i in range(len(codigo)):
            while len(codigo) < 5:
                print("\nERROR...")
                codigo = input("El codigo tiene que ser numerico y de cinco digitos: ")
            match codigo[i]:
                case "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9":
                    ingreso_valido = True
                case _:
                    codigo = input("ERROR, El codigo tiene que ser numerico: ")
                    ingreso_valido = False
                    break
    return codigo

def buscar_vuelo_por_codigo(vuelos: list) -> list:
    codigo = input("\ningrese el codigo del vuelo a buscar: ")

    for i in range(len(vuelos)):
        if vuelos[i][0] == codigo:
            resultado = vuelos[i]
            return resultado
        else:
            return "El vuelo no existe"

def buscar_vuelo_mas_caro(vuelos: list) -> list:
    precio_maximo = float('-inf')
    fila_mas_cara = []

    for i in range(len(vuelos)):
        for j in range(len(vuelos)):
            if vuelos[i][2] > precio_maximo:
                precio_maximo = vuelos[i][2]
                fila_mas_cara = vuelos[i]
    return fila_mas_cara

def buscar_vuelo_mas_barato(vuelos: list) -> list:
    precio_minimo = float('inf')
    fila_mas_barata = []

    for i in range(len(vuelos)):
        for j in range(len(vuelos)):
            if vuelos[i][2] < precio_minimo:
                precio_minimo = vuelos[i][2]
                fila_mas_barata = vuelos[i]
    return fila_mas_barata

def mostrar_vuelos_mayores_a_valor(vuelos: list) -> list:
    vuelos_mayores_a_valor = []

    for i in range(len(vuelos)):
            if vuelos[i][2] > 100000:
                vuelos_mayores_a_valor += [vuelos[i]]
    return vuelos_mayores_a_valor