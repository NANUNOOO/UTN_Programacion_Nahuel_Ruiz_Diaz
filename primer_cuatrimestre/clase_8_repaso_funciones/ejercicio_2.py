def calcular_area(base=1, altura=1):
    area = base * altura
    return area

base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))
print(calcular_area())