'''Faça um programa que peça uma nota, entre zero e dez. Mostre uma
mensagem caso o valor seja inválido e continue pedindo até que o usuário
informe um valor válido.'''

while True:
    nota = int(input('Digite uma nota de 0 a 10: '))

    if 0 <= nota <=10:
        print('Você digitou uma nota correta')
        break  
    else:
        print('Nota invalida, digite uma nota de 0 a 10')