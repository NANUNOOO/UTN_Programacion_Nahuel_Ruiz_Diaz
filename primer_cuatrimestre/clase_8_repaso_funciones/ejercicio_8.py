def primo_o_compuesto(numero):
    estado = true
    if numero < 2: 
        return "error"
    for in range(2,numero):
        estado= false
        break
return estado
valor_numero = int(input ("ingrese un numero"))
resultado = primo_o_compuesto(valor_numero)
print(resultado)