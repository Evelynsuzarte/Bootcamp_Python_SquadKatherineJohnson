"""

Escreva um script que pergunta ao usuário se ele deseja converter
uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para
cada opção, crie uma função.
Extra: Crie uma terceira, que é um menu para o usuário escolher a
opção desejada, onde esse menu chama a função de conversão
correta

"""

def celsius(temp):
    c = (temp-32)/1.8
    return c

def fahrenheit(temp):
    f = (1.8*temp)+32
    return f

def menu():
    print("**** CONVERSOR DE TEMPERATURA ****")
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para celsius")
    opcao = int(input("Selecione\n"))
    temp = float(input("Digite a temperatura: "))
    if opcao == 1:
        resultado = fahrenheit(temp)
        print(f"Resultado da conversão: {resultado} F")
    elif opcao == 2:
        resultado = celsius(temp)
        print(f"Resultado da conversão: {resultado} C")
                

menu()