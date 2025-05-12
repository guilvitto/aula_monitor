nomes_A=[]
for i in range(0,5):
    nomes=input("Digite 5 nomes: ")
    if nomes[0] == "a" or nomes[0] == "A":
        nomes_A.append(nomes)
print(f"Esses nomes tem a letra A: \n{nomes_A}")