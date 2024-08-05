"""
9. O programa deve calcular e apresentar a quantidade de números pares e
ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
informar o valor zero. Certifique-se de incluir validações para garantir que
apenas números positivos sejam considerados na contagem e cálculos.
"""
from time import sleep

numeros_pares = 0
numeros_impares = 0
while True:
    
    try:

        numero = int(input("Digite os números que deseja inserir na listagem ou digite 0 para sair e -1 para mostrar os resultados: "))

        
        if numero == 0:
            print("Obrigada por utilizar nossos programas, saindo...")
            sleep(0.7)
            break
        elif numero == -1:
            print(f"Você digitou {numeros_pares} números pares e {numeros_impares} números ímpares.")
            sleep(0.7)
            break
        elif numero < -1:
            print("O valor não pode ser negativo.")
            continue
        
        elif numero % 2 == 0:
            numeros_pares += 1
            continue
        else:
            numeros_impares += 1
            continue
        
    except ValueError:
        print("Valor inválido.")
