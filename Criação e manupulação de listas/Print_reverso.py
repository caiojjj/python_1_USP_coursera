list_numero = []
numero = 1
while numero > 0:
    numero = int(input("Digite um número inteiro positivo: "))
    if numero != 0:
        list_numero.append(numero)

n = len(list_numero) - 1
while n >= 0:
    print(list_numero[n])
    n -= 1