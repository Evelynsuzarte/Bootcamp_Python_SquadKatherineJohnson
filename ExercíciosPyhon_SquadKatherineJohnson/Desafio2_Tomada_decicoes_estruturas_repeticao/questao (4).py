"""
4. Implemente um programa que classifique um aluno com base em sua
pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10. Se
a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é
reprovado.
"""
# Solicitando a pontuação do aluno
nota = float(input("Digite a pontuação do aluno (0 a 10): "))

# Classificando e exibindo o resultado
if 0 <= nota <= 10:
    if nota >= 7:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
else:
    print("Nota inválida.")
