'''Utilizando listas faça um programa que faça 5 perguntas para uma
pessoa sobre um crime.
As perguntas são:
""Telefonou para a vítima?""
""Esteve no local do crime?""
""Mora perto da vítima?""
""Devia para a vítima?""
""Já trabalhou com a vítima?""
O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como
""Assassino"".
Caso contrário,ele será classificado como""Inocente"".
'''
perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

respostas = []

print('Responda as perguntas digitando 1 para sim e 2 para não!')

for pergunta in perguntas:
    resposta = int(input(pergunta + " "))
    if resposta == 1:
        respostas.append(resposta)

num_respostas_positivas = len(respostas)

if num_respostas_positivas == 5:
    classificacao = "Assassino"
elif 3 <= num_respostas_positivas <= 4:
    classificacao = "Cúmplice"
elif num_respostas_positivas == 2:
    classificacao = "Suspeita"
else:
    classificacao = "Inocente"

print(f"A classificação final é: {classificacao}")