''' 2 - Reverso do número.
Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo:127->721.'''

def numero_invertido (num):
    num_str = str(num)
    num_str_invertido = num_str[::-1]
    inteiro = int(num_str_invertido)
    return inteiro

num = int(input("Digite o número que será invertido: "))
numero_invertido1 = numero_invertido(num)
print(f'O número invertido é: {numero_invertido1}')