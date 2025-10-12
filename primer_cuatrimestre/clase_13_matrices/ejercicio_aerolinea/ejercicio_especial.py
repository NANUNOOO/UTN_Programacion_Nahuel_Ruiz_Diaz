"""
Sistema de Gestión de Vuelos  Aerolínea “SkyWings"
La aerolínea SkyWings necesita un sistema básico para administrar la información de sus vuelos. Cada vuelo contiene los siguientes datos:

Código del vuelo (número de al menos 5 dígitos en formato string)
Ciudad de destino
Precio del boleto

La información se almacenará en una matriz (lista de listas), donde cada fila representa un vuelo y las columnas contienen los datos mencionados.
Requerimientos del sistema:

1-Menú Principal  ----------------

Mostrar un menú con las siguientes opciones:
Cargar vuelo/s
Buscar vuelo por código
Mostrar vuelo más caro
Mostrar vuelo más barato
Mostrar vuelos con precio mayor a 100000
Salir

2-Cargar vuelo  ---------------

Crear una función que permita al usuario ingresar los datos de uno o más vuelos.
El usuario debe indicar cuántos vuelos desea cargar.
Por cada vuelo se solicitará:
Código del vuelo: debe ser un número entero de 5 o más dígitos. Si no cumple, debe pedirse nuevamente.
Ciudad de destino.
Precio del boleto.
La carga se realiza en una matriz predefinida, sin usar métodos de listas.

3-Buscar vuelo por código -----------------
Permitir al usuario ingresar el código de un vuelo.
Si existe, mostrar todos los datos correspondientes.

4-Mostrar vuelo más caro ------------------
Crear una función que recorra la matriz y muestre el vuelo con el precio más alto.

5-Mostrar vuelo más barato ----------------- 
Crear una función que recorra la matriz y muestre el vuelo con el precio más bajo.

6-Mostrar vuelos con precio mayor a 100000
Mostrar todos los vuelos cuyo precio supere ese valor.
"""
import funciones.menu as menu

vuelos = []

print(menu.mostrar_menu(vuelos))