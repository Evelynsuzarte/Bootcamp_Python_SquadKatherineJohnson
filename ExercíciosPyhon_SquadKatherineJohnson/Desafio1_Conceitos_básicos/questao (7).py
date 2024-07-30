'''
Solicite ao usuário o peso em kg e a altura em metros. Calcule e
imprima o Índice de Massa Corporal (IMC) usando a fórmula:
IMC = peso / (altura x altura).
'''

peso = float(input('Informa o seu peso: '))
altura = float(input('Informa a sua altura em metros (Ex 1.72): '))

imc = peso / (altura * altura)

if imc <= 18.5:
    resultado = ('Abaixo do peso')
elif imc <= 24.9:
    resultado = ('Peso normal')
elif imc <= 29.9:
    resultado = ('Sobrepeso')
elif imc <= 34.9:
    resultado = ('Obesidade Grau 1')
elif imc <= 39.9:
    resultado = ('Obesidade Grau 2')
else:
    resultado = ('obesidade mórbida')

print(f'Seu IMC é {imc:.2f}. {resultado}.')