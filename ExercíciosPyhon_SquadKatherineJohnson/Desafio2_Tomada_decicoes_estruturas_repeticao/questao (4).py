"""
4. Implemente um programa que classifique um aluno com base em sua
pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10. Se
a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é
reprovado.
"""
while True:
    try:

    
            nota = int(input("Por favor, a nota do aluno: "))

            if nota > 10 or nota < 0:
                
                print("A nota precisa ser maior que 0 e menor que 10.\n")
                continue
            
            elif nota >= 7:
                print("Aluno aprovado!")
            
            else:
                print("Aluno reprovado.")
            
    except ValueError:
        print("Valor inválido. Tente novamente.")
        continue
