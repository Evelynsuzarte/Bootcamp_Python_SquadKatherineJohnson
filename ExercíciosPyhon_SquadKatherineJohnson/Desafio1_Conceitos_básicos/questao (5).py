"""
11. Escreva um programa que calcule o salário líquido. 
Lembrando de declarar o salário bruto e o percentual de desconto do Imposto de Renda.

    ● Renda até R$ 1.903,98: isento de imposto de renda;
    ● Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
    ● Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
    ● Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
    ● Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.
    
# """

try:
    salario_bruto = float(input("Por favor digite o seu salário: R$"))
    imposto_renda = 0
    
    if salario_bruto < 0:
        print("O seu salário não pode ser um valor negativo.")
        
    else:
        if salario_bruto <= 1903.98:
            print("Isento de imposto de renda")
            
        elif salario_bruto >= 1903.99 and salario_bruto <= 2826.65:
            imposto_renda = salario_bruto * (7.5/100)
            
        elif salario_bruto >= 2826.66 and salario_bruto <= 3751.05:
            imposto_renda = salario_bruto * (15/100)
            
        elif salario_bruto >= 3751.66 and salario_bruto <= 4664.68:
            imposto_renda = salario_bruto * (22.5/100)
            
        else:
            imposto_renda = salario_bruto * (27.5/100)
            
        salario_liquido = salario_bruto - imposto_renda
        
        print(f"O seu desconto do imposto de renda foi de R${imposto_renda :.2f} e o seu salário líquido será R${salario_liquido :.2f}.")
    
except ValueError:
    print("Este valor é inválido.")
