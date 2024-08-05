"""
Escreva um programa que calcule o tempo de uma viagem. 
Faça um comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração:
    ● avião = 600 km/h
    ● carro = 100 km/h
    ● ônibus = 80 km/h

"""

def calcula_tempo(distancia):
    veiculos_velocidade_por_hora = {
        "avião" : 600,
        "carro" : 100,
        "ônibus" : 80,
    }
    
    for veiculo, velocidade_hora in veiculos_velocidade_por_hora.items():
        tempo_viagem_horas = distancia / velocidade_hora

        if distancia < velocidade_hora:
            tempo_viagem_minutos = tempo_viagem_horas * 60
            print(f"Se você for de {veiculo}, vai levar {tempo_viagem_minutos:.0f} minutos para chegar ao seu destino.")
        else:
            print(f"Se você for de {veiculo}, vai levar {tempo_viagem_horas:.0f} horas para chegar ao seu destino.")

try: 
    distancia = float(input("Olá viajante, qual é a distância do seu percurso? "))
    if distancia <= 0:
        print("A distância precisa ser maior do que zero.")
    else:
        calcula_tempo(distancia)

except ValueError:
    print("O valor precisa ser válido.")
