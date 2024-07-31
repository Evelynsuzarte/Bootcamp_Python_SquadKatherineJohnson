"""
    Escreva um programa que calcule o tempo de uma viagem. Faça um
    comparativo do mesmo percurso de avião, carro e ônibus.
    Levando em consideração:
    ● avião = 600 km/h
    ● carro = 100 km/h
    ● ônibus = 80 km/h
"""

distancia = float(input("Digite a distância em km até o destino:"))


aviao = distancia/600
carro = distancia/100
onibus = distancia/80

print(f"Tempo com:\nAvião: {aviao} horas\nCarro: {carro} horas\nÔnibus: {onibus} horas")