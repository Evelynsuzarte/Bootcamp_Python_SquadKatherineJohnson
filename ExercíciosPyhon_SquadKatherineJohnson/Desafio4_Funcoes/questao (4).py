'''
Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
Considere a tabela de conversão abaixo:
Dólar Americano: R$ 4,91
Peso Argentino: R$ 0,02
Dólar Australiano: R$ 3,18
Dólar Canadense: R$ 3,64
Franco Suiço: R$ 0,42
Euro: R$ 5,36
Libra esterlina: R$ 6,21'''

taxas_conversao = {
    "Dólar Americano": 4.91,
    "Peso Argentino": 0.02,
    "Dólar Australiano": 3.18,
    "Dólar Canadense": 3.64,
    "Franco Suiço": 0.42,
    "Euro": 5.36,
    "Libra esterlina": 6.21
}

def calculo_moeda(carteira, taxa):
    return carteira / taxa

valor_reais = float(input("Digite o valor em reais que você tem na carteira: "))

print("\nCom R$ {:.2f}, você poderia comprar aproximadamente:".format(valor_reais))
for moeda, taxa in taxas_conversao.items():
    valor_moeda = calculo_moeda(valor_reais, taxa)
    print("- {:.2f} {}".format(valor_moeda, moeda))
