"""Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos"""

clave_correcta= "hola1234"
intentos = 0

ingreso_clave = input("ingrese su contraseña: ")

while ingreso_clave != clave_correcta and intentos < 3:
    intentos += 1
    ingreso_clave = input("ERROR, Reingrese su contraseña: ")

if intentos >= 3:
    print("Numero de intento exedidio, intentelo mas tarde.")
else:
    print("contraseña correcta.")