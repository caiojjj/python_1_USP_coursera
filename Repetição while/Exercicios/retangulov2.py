largura = int(input("Digite a largura do retangulo: "))
altura = int(input("Digite a altura do retangulo : "))
maximo = altura
while altura > 0:
    i = largura
    if altura == maximo or altura == 1:
        while i - 1 > 0:
            print("#", end = "")
            i -= 1
        print("#\n", end = "")
        i = largura
    elif altura != maximo and altura != 0:
        print("#", end = "")
        while (i - 2) > 0:
            print(" ", end = "")
            i -= 1 
        print("#")
    altura -= 1