numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
def somar_pares(lista):
    soma =0 
    for numero in (lista):
        if numero % 2 == 0:
            soma += numero
    return soma

# Testes
print(somar_pares(numeros))  
