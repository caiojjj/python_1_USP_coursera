fatorial = int(input("Digite um valor de fatorial: "))

def Fatorial(fatorial):
    i = fatorial
    if fatorial == 0:
     print(1)
    else:
        while i > 0:
            if i == 1:
                break
            i -= 1
            fatorial = fatorial * i
    return fatorial
        
print(Fatorial(fatorial))