"""Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla."""

contador = 0
suma = 0

while contador < 5:    
    numero = int(input("Ingrese un numero: "))
    suma += numero
    contador += 1
    
promedio = suma / contador  

print("la suma es:",suma)
print("su promedio es:",promedio)