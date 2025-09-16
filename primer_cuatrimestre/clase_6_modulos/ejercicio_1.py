"""escribe una funcion llamada calculo_de_imc que reciva una altura y el peso e indique el indice de masa corpoal(IMC) de una persona.

.peso inferior al normal:imc de 18,5
.normal:imc entre 18,5-24,9
.peso superior al normal: imc entre 25,0-29,9
.obesidad:imc > de 30,9"""

peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))
def calculo_de_imc(peso, altura):
    
    mensaje = ""
    imc = peso / altura ** 2

    if imc < 18.5:
        mensaje = "Su indice es inferior al normal"

    elif imc > 18.5 and imc < 24.9:
        mensaje = "Su indice es normal"

    elif imc > 25.0 and imc < 29.9:
        mensaje = "Su indice es superior a lo normal"

    elif imc > 30.9:
        mensaje = "su indice esta dentro del rango de obesidad"
    
    return print(imc,mensaje)

calculo_de_imc(peso,altura)

