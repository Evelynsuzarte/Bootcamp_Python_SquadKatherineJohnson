"""
4. Receba do usuário a quantidade de litros de combustível consumidos e a distância percorrida. Calcule e imprima o consumo médio em km/l.
"""

try:
    while True:
        litros = int(input("Quantos litros de combustível você consumiu neste percurso? "))
        
        if litros <= 0:
            print("Você precisa inserir um valor maior do que zero.")
            break
            
        distancia = int(input("Qual foi a distância percorrida? "))
        
        if distancia <= 0:
            print("A distância não pode ser menor do que zero. ")
            break

        media = distancia/litros

        print(f"O seu veículo fez uma média de {media}km/L")

except ValueError:
    print("É necessário que seja inserido um valor válido.")
