cont = 0
frase = input("Digite a frase: ")
for i in frase.lower():
    if i  == "a":
        cont+=1
print(f"{cont} letras A na frase! ")

