def area_retangulo(a,b):
    return a*b
def exibir_valor(a,b,função):
  resultado = função(a,b)
  print(f'o resultado da operação e {resultado}')

exibir_valor(5,10,area_retangulo)