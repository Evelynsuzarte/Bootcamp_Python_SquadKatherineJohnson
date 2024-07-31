#4. Crie um dicionário representando contatos (nome, telefone). Permita ao usuário procurar por um contato pelo nome.

contatos = {"Silvia": "1234-5678", "Milena": "2345-6789", "Carlos": "3456-7890", "Maria": "4567-8901"}


def procurar_contato(nome):
    if nome in contatos:
        return f"Telefone de {nome}: {contatos[nome]}"
    else:
        return "Contato não encontrado."

def procurar_contato_por_telefone(telefone):
    for nome, numero in contatos.items():
        if numero == telefone:
            return f"Nome do contato: {nome}"
    return "Número de telefone não encontrado."

n = -1
while n != 3:    
    print("1.- Busqueda pelo nome ")
    print("2.- Busqueda pelo número de telefone ")
    print("3.- Sair ")
    n = int(input("Digite a opção desejada: "))
    if n == 1:
        nome_procurado = input("Digite o nome do contato que deseja procurar: ")
        resultado = procurar_contato(nome_procurado)
        print(resultado)
    elif n == 2:
        telefone_procurado = input("Digite o número de telefone que deseja procurar: ")
        resultado = procurar_contato_por_telefone(telefone_procurado)
        print(resultado)
    elif n == 3:
        break