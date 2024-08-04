"""8. Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês.Calcule e mostre o total do seu
salário no referido mês.
"""
sph = float(input("Quanto você recebe por hora? ")) #salario por hora
hora = int(input('Quantas horas você trabalhou esse mês? '))
total = hora * sph
print(f'Trabalhando {hora} horas por mês e recebendo R${sph:.2f} por hora, você recebeu R${total:.2f} esse mês.')