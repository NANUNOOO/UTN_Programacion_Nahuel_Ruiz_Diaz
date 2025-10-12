import funciones.logica

def mostrar_menu(vuelos):
    ingreso = False

    while not ingreso:
        print("\n1-Cargar vuelo/s\n2-Buscar vuelo por código\n3-Mostrar vuelo más caro\n4-Mostrar vuelo más barato\n5-Mostrar vuelos con precio mayor a 100000\n6-Salir")
        opcion = input("\n\nINGRESE EL NUMERO DE OPCION: ")
        if opcion == "1":
            print(funciones.logica.cargar_vuelos(vuelos))
        elif opcion == "6":
            ingreso = True
        elif len(vuelos) < 1:
            print("---Ingrese vuelos para elejir opciones---")
            ingreso = False
        elif opcion == "2":
            print(funciones.logica.buscar_vuelo_por_codigo(vuelos))
        elif opcion == "3":
            print(funciones.logica.buscar_vuelo_mas_caro(vuelos))
        elif opcion == "4":
            print(funciones.logica.buscar_vuelo_mas_barato(vuelos))
        elif opcion == "5":
            print(funciones.logica.mostrar_vuelos_mayores_a_valor(vuelos))
    return "\nFIN"
