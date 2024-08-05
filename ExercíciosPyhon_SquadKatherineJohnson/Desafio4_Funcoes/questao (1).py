"""
1. Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
"""

def soma_tres_numeros(primeiro, segundo, terceiro):
    soma = primeiro + segundo + terceiro
    return soma


try:
    
    print("Vamos somar três números! \n")

    primeira_entrada = float(input("Digite o primeiro número para a soma: "))
    segunda_entrada = float(input("Digite o segundo número para a soma: "))
    terceira_entrada = float(input("Digite o terceiro número para a soma: "))

    resposta = soma_tres_numeros(primeira_entrada,segunda_entrada,terceira_entrada)
    
    print(f"Aqui está o resultado: {primeira_entrada :.2f} + {segunda_entrada :.2f} + {terceira_entrada :.2f} = {resposta :.2f}")
    
except ValueError:
    print("Valor inválido.")
    
    
