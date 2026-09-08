def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def exibir_temperatura(funcao_conversao, celsius):
    resultado = funcao_conversao(celsius)
    print(f"{celsius}°C em Fahrenheit é {resultado:.2f}°F")

exibir_temperatura(celsius_para_fahrenheit, 100)