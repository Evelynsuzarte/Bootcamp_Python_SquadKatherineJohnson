''' 10 - Faça um programa que lê três números inteiros e os mostra em ordem
crescente.'''

interios1 = input ("Digite três números, separados por virgula: ")
num_str = interios1.split(',')

convert = [int(i) for i in num_str]

convert.sort()
print(convert)