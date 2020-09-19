import math

ax = int(input("Digite o coeficiente principal da função de segundo grau: "))
bx = int(input("Digite o coeficiente secundario da funão de segundo grau: "))
c = int(input("Digite o coeficiente independente da equação de segundo grau: "))

if ax != 0:
    delta = bx**2 - 4 * ax * c
    print("O valor de Delta é: ",delta)
    if delta == 0:
        raiz = (-bx + math.isqrt(delta)) / (2*ax)
        print("Duas raizes reais e iguais:", raiz)
    elif delta > 0:
        raizPri = (-bx + math.isqrt(delta)) / (2*ax)
        raizSeg = (-bx - math.isqrt(delta)) / (2*ax)
        print("As raizes são : ", raizPri, raizSeg)
    elif delta < 0:
        print("Número imaginario!")
else:
    print("Não é umas equação do segundo grau!")