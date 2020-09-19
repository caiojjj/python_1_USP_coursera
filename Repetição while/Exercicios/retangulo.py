largura = int(input("Digite a largura do retangulo: "))
altura = int(input("Digite a altura do retangulo : "))

while altura > 0:
    i = largura
    while i >0:
        print("#", end = "")
        i -= 1
    print()
    altura -= 1