"""
1. Faça um Programa que peça dois números, realize as principais
operações soma, subtração, multiplicação, divisão
"""

try:
    primeiro_numero = int(input("Digite um número inteiro: "))
    segundo_numero = int(input("Digite outro número inteiro: "))

    soma = primeiro_numero + segundo_numero

    subtracao = primeiro_numero - segundo_numero
    
    multiplicacao = primeiro_numero * segundo_numero

    divisao = primeiro_numero / segundo_numero

    print(f' A soma entre {primeiro_numero} e {segundo_numero} é: {soma}')
    print(f' A subtração entre {primeiro_numero} e {segundo_numero} é: {subtracao}')
    print(f' A multiplicação entre {primeiro_numero} e {segundo_numero} é: {multiplicacao}')
    print(f' A divisão entre {primeiro_numero} e {segundo_numero} é: {divisao}')
    
except ValueError:
    print("O valor inserido precisa ser um número inteiro.")