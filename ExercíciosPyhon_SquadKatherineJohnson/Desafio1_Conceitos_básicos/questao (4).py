"""
4. Receba do usuário a quantidade de litros de combustível consumidos e a distância percorrida. Calcule e imprima o consumo médio em km/l.
"""
# Solicitando a quantidade de litros consumidos e a distância percorrida
litros_consumidos = float(input("Digite a quantidade de litros consumidos: "))
distancia_percorrida = float(input("Digite a distância percorrida em quilômetros: "))

# Calculando o consumo médio
consumo_medio = distancia_percorrida / litros_consumidos

# Exibindo o resultado
print(f"O consumo médio é de {consumo_medio:.2f} km/l.")
