# 6. Crie um programa que solicite ao usuário um login e uma senha. O programa deve permitir o acesso apenas se o usuário for "admin" 
# e a senha for "admin123", caso contrário imprima uma mensagem de erro.

login = input("Digite seu login: ")


if login == "admin":
    senha = input("Digite sua senha: ")
    if senha == "admin123":
        print("Acesso autorizado!")
    else:
        print("Senha incorreta!")
else:
    print("Usuario não autorizado")