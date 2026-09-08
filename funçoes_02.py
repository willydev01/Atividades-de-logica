def somar(a, b):
    return a + b


def subtrair(a,b):
    return a - b

def Multiplicação(a, b):
    return a*b

def divisão(a,b):
    return a / b 

def divisãoint(a,b):
    return a // b 

def exibir_resultado(a, b, função):
    resultado = função(a, b)
    print(f'o resultado da operação e = {resultado}')


exibir_resultado(50,10, somar)
exibir_resultado(900, 10, subtrair)
exibir_resultado(200,5, Multiplicação)
exibir_resultado(400,8, divisão)
exibir_resultado(655,10, divisãoint)