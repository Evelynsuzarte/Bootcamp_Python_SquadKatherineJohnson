"""
2. Peça ao usuário para informar o ano de nascimento. Em seguida, calcule e imprima a idade atual.
"""

try:
        
    ano = int(input('Digite seu ano de nascimento com os quatro dígitos (Por exemplo 1995): '))

    if len(str(ano)) == 4 and ano >= 1924:
        calculo_idade_com_aniversario = 2024 - ano
        calculo_idade_sem_aniversario = 2023 - ano

        print(f'Se você já fez aniversário neste ano de 2024 então a sua idade é: {calculo_idade_com_aniversario}')
        print(f'Se você ainda não fez aniversário neste ano de 2024 então a sua idade é: {calculo_idade_sem_aniversario}')
    else:
        print("Você precisa inserir um valor válido.")
                
except ValueError:
        print("O valor inserido precisa ser um número inteiro.")
        
        