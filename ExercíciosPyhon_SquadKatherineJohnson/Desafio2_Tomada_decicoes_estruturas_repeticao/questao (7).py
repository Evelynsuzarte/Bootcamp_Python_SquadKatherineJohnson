"""
7. Desenvolver um programa que solicite a idade do usuário e identifique se
ele é uma criança, um adolescente, adulto ou idoso.

- Criança: 0 a 12
- Adolescente: 13 a 17
- Adulto: 18 aos 59
- Idoso: 60 aos 110
"""

try:
    idade = int(input("Digite a sua idade: "))
    
    if idade < 0 or idade > 110:
        print ("A idade precisa ser maior do que 0 e menor do que 110.")
        
    elif idade >= 0 and idade <= 12:
        print(f"Você é uma criança, pois tem {idade} anos. Brinque bastante!")
    
    elif idade >= 13 and idade <= 17:
        print(f"Você é um adolescente, pois tem {idade} anos. Curta os melhores momentos da sua vida")
        
    elif idade >= 18 and idade <= 59:
        print(f"Você é um aduldo, pois tem {idade} anos. Aproveite as responsabilidades.")
    
    elif idade > 60 and idade <= 110:
        print(f"Você é um idoso, pois tem {idade} anos. Tenha experiências incríveis!")

except ValueError:
    print("Este não é um valor válido.")