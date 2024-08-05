"""
2. 
- Faça um Programa que peça as quatro notas de 5 alunos, 
- calcule e armazene numa lista a média de cada aluno,
- imprima o número de alunos com média maior ou igual a 7.0.
"""


num_alunos = 5
num_notas = 4
medias = []

for i in range(num_alunos):
    notas = []
    print(f"Notas do aluno {i + 1}:")
    for j in range(num_notas):
        nota = float(input(f"Digite a nota {j + 1}: "))
        notas.append(nota)
    media = sum(notas) / num_notas
    medias.append(media)

alunos_acima_media = sum(1 for media in medias if media >= 7.0)
print(f"Número de alunos com média maior ou igual a 7.0: {alunos_acima_media}")
