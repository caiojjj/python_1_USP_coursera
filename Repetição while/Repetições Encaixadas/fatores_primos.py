
inteiro = int(input("Digite um número inteiro não negativo: "))

fator = 2
muliplicidade = 0
while inteiro > 1:
    while inteiro % fator == 0:
        muliplicidade += 1
        inteiro = inteiro / fator
        print("Fator: ", fator, "Multiplicidade", muliplicidade)
    fator += 1
    muliplicidade = 0
