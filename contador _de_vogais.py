vogais = ['a','e','i','o','u']

def contar_vogais(palavra):
    contador = 0
    for letra in palavra:
        if letra in vogais:
            contador += 1
    return contador

print(contar_vogais('avião') ) 
print(contar_vogais('abacaxi') ) 
print(contar_vogais('feijão') )
print(contar_vogais('coelho') )
print(contar_vogais('galo') )   
        
