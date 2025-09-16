

def numero_maximo(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num3:
        return num3
    else:
        return num3


print(numero_maximo(58,18,6))