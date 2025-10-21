"""
Implementa un sistema para administrar préstamos de libros usando dos listas relacionadas:

Funcionalidades requeridas:

prestar_libro(titulo):
Busca el libro y marca su disponibilidad como False
Si no existe o no está disponible, muestra un 

devolver_libro(titulo):
Busca el libro y actualiza su estado a True
Maneja errores si el libro no pertenece a la biblioteca

mostrar_estado():
Lista todos los libros con su estado actual

"""

libros = ["Cien años de soledad", "1984", "El principto", "Don quijote"]
disponibles = [True, True, True, True]

titulo = input("Ingrese el libro: ")

def prestar_libro(titulo, libros, disponibles):
    indice = libros.index(titulo)
    for i in range(len(libros)):
        if disponibles[indice]:
            disponibles = False
            print(f"Se encontro el libro {titulo}.")
        elif disponibles[indice] == False:
            print(f"ERROR, el libro {titulo} fue prestado.")
        else:
            print("ERROR, Libro no encontrado...")

def devolver_libro(titulo, libros, disponibles):
    indice = libros.index(titulo)
    for i in range(len(libros)):
        if not disponibles[indice]:
            disponibles = True
            print(f"Se encontro el libro {titulo} y fue devuelto.")
        elif disponibles[indice] == True:
            print(f"ERROR, el libro {titulo} no fue prestado.")
        else:
            print("ERROR, Libro no encontrado...")


print(prestar_libro(titulo, libros, disponibles))
print(devolver_libro(titulo, libros, disponibles))
