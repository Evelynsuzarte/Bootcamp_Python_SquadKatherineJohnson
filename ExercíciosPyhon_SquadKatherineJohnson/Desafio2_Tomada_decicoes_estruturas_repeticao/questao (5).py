""" 
5.Desenvolva um programa que solicite ao usuário os comprimentos dos três lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.

* equilátero: todos os lados com o mesmo valor
* isósceles: dois lados com o mesmo valor
* escaleno: todos os lados com medidas distintas.

"""

try:
    lado_um = float(input("Digite o primeiro lado do triângulo: "))
    lado_dois= float(input("Digite o segundo lado do triângulo: "))
    lado_tres = float(input("Digite o terceiro lado do triângulo: "))
    
    if lado_um == lado_dois and lado_dois == lado_tres and lado_tres == lado_um:
        print("Este é um triângulo equilátero.")
        
    elif lado_um != lado_dois and lado_dois != lado_tres and lado_tres != lado_um:
        print("Este é um triângulo escaleno.")
        
    else:
        print("Este é um triângulo isósceles.")

except ValueError:
    print("Valor inválido.")
