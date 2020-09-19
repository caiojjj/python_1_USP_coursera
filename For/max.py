def minima(temps):
    min = 0
    i = 0
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i += 1
    return min

def MinMax(temperaturas):
    print("A menor temperatura do mês foi: ", minima(temperatura), "ºC.")
    print("A maior temperatura fo mês foi: ", maxima(temperaturas), "ºC.")

def testa_minima():
    print("Iniciando os testes")
    temp = [0]
    if minima(temp) != 0:
        print("Valor errado para o array", temp)
    temp = [0, 0, 0, 0, 0, 0]
    if minima(temp) != 0:
        print("Valor errado para o array", temp)
    print("Finalizando os testes")
    