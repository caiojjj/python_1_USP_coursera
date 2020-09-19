valor = input("Digite o numero que terar seus elementos somados: ")
i = len(valor)
valor = int(valor)
soma = 0
while i != 0 :
    soma += valor % 10
    valor = valor // 10
    i -= 1
print(soma)
    