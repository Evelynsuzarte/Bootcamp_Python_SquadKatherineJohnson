'''1. Faça um programa, com uma função que necessite de três
argumentos, e que forneça a soma desses três argumentos.
'''
def soma(a, b, c):
    print(f'A soma de {a}, {b} e {c}, é {a+b+c}.')

n1 = int(input('Insira um número - '))
n2 = int(input('Insira outro número - '))
n3 = int(input('Insira mais um número - '))
soma(n1,n2,n3)
