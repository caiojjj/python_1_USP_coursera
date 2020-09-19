valor = input("Digite um numero: ")
i = len(valor)
valor = int(valor)
temAdjacente = False
adjacente = 0
anterior = 1
while i > 0:
    adjacente = valor % 10
    if adjacente == anterior:
        temAdjacente = True
        break
    anterior = adjacente
    valor = valor // 10
    i -= 1

if temAdjacente:
    print("Os números adjacentes são:", adjacente, "e" ,anterior, "nas posições", i, "e", i+1)
else:
    print("Não possui números adjacentes.")   
    