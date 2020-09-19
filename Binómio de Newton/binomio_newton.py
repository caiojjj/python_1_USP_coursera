def Fatorial(fatorial):
    if fatorial == 0:
        return 1
    else:
        i = fatorial
        while i > 1:
            i -= 1
            fatorial = fatorial * i
    return fatorial

def Numero_binomial(n, k):
    if n >= k:
        resul = Fatorial(n) // (Fatorial(k) * Fatorial(n - k))
        print(resul)
    else:
        print("Valores invalidos, K! não deve ser maior que N!.")

n = int(input("Digite o valor de N!: "))
k = int(input("Digite o valor de K!: "))
print(Numero_binomial(n, k))
