while True:
    segredo = 75
    resp = int(input(f"Digite um númrero para adivinhar: "))
    if resp < segredo:
        print("O número é maior!")
    elif resp > segredo:
        print("O número é menor!")
    else:
        print("Parabéns! Você acertou!")
        break