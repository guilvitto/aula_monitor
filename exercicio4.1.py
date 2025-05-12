soma = 0
for i in range(5):
    nota = int(input("Digite a nota: "))
    soma= soma + nota
media = soma/5
if media >= 7:
    print("Aprovado!")
elif 4<=media<=7:
    print("Recuperação!")
elif 0<media<4:
    print("Reprovado!")
else:
    print("Número inválido!")