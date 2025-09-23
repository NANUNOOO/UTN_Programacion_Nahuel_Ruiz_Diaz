# Un mercado nos solicito que quiere saber el valor total de sus ventas del dia, que son las siguientes:
# 350.50, 1400.99, 450, 325.49, 500,120.20
# Ademas quiere saber el promedio de las mismas.
# Mostrar ambas solicitudes por pantalla.

suma = 0

lista = [350.50, 1400.99, 450, 325.49, 500,120.20]

# Suma
for i in range(len(lista)):
    suma += lista[i]

# Promedio
for i in range(len(lista)):
    promedio = suma / len(lista)

print(suma)
print(promedio)