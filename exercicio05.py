i=""
while i!="1234":
    senha = input("Digite a senha de acesso: ")
    if senha == "1234":
        i=senha
        print("Acesso Liberado!")
    else:
        print("Acesso negado, tente novamente!")
