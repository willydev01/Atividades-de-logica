numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def filtar_pares(lista):

    for numeros in (lista):
        if numeros % 2 == 0:   
            print(f'e par {numeros}')
        else:
            print(f'e impar {numeros}')
filtar_pares(numeros)
    