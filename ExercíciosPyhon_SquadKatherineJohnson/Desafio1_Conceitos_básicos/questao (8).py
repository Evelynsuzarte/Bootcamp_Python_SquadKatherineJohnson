"""
Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês.Calcule e mostre o total do seu
salário no referido mês.
"""

def calcula_salario(valor_por_hora, horas_trabalhadas):
    salario = valor_por_hora * horas_trabalhadas
    return salario

try:

    valor_hora = float(input("Qual é o valor ganho por hora? "))
    quantidade_horas = int(input("Quantas horas você trabalhou no mês? "))
    if valor_hora <= 0:
        print("O valor precisa ser maior que zero.")
    else:
        salario = calcula_salario(valor_hora, quantidade_horas)
        print(f'Você trabalhou {quantidade_horas} horas neste mês e a previsão para o seu salàrio é de R${salario:.2f}')
