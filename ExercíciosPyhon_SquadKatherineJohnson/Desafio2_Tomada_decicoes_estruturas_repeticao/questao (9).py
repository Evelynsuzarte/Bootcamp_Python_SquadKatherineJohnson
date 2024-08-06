
"""9. O programa deve calcular e apresentar a quantidade de números pares e
ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
informar o valor zero. Certifique-se de incluir validações para garantir que
apenas números positivos sejam considerados na contagem e cálculos.
"""
n = int(input("Insira um número - "))
par, impar = 0, 0 
while n!= 0:
    if n>0 and n%2 == 0:
        par += 1
    elif n > 0 and n%2 == 1:
        impar += 1
    n = int(input("Insira um número - "))
print(f"Você inseriu o número zero. No total, foram inseridos {impar} números ímpares e {par} números pares positivos.")
