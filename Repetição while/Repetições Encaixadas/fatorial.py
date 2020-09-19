fatorial = 1

while fatorial >= 0:
    fatorial = int(input("Digite um número inteiro poditivo: "))
    if fatorial == 0:
        fatorial = 1
        print(fatorial)
    elif fatorial >0:
        i = fatorial
        while i > 1:
            i -= 1
            fatorial = fatorial * i
        print(fatorial)