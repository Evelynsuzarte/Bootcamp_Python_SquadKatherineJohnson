#EXERCICIO 3
#Faça um Programa que peça a quantidade de quilômetros, transforme em metros, centímetros e milímetros

km = float(input("Digite o número de kilometros que deseja convertir: "))
metros = km * 1000
centim = metros * 100
milim = centim * 10
print(f'{km} km são: {metros} metros, ')
print(f'{km} km são: {centim} centimetros')
print(f'{km} km são: {milim} milimetros')