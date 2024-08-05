"""
3. Crie um dicionário representando um carrinho de compras.
Adicione produtos (chaves) e quantidades (valores) ao carrinho.
Calcule o total do carrinho de compra.
"""

try:
    
    carrinho_de_compras = {
        "arroz" : 4.50,
        "feijão": 7.00,
        "macarrão" : 6.00,
        "leite" : 4.00,
        "ovos": 12.00,
        "pizza" : 16.00,
        "shampoo": 20.00,
        "sabão" : 20.00,
        "pasta de dente" : 3.00,
        "cotonete": 2.00,
        "chocolate": 5.00
    }
    
    total_carrinho = 0
    for item in carrinho_de_compras:
        total_carrinho += carrinho_de_compras[item]
        
    print(f"O seu carrinho tem um total de {len(carrinho_de_compras)} itens e o valor da sua compra é: R${total_carrinho :.2f}")

except ValueError:
    print("Valor inválido.")
except KeyError:
    print("Existe algum problema com o seu dicionário.")
