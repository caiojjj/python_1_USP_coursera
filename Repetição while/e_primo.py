def ePrimo(x):
    fator = 2
    while x % fator != 0 and x < fator:
        fator += 1
    if x % fator == 0:
        return False
    else:    
        return True

inteiro = int(input("Digite um número inteiro não negativo: "))
while inteiro > 0:
    if ePrimo(inteiro):
        print("É primo.")
    else:
        print("Não é primo.")
    inteiro = int(input("Digite um número inteiro não negativo: "))