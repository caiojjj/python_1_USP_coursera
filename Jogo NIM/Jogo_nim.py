def print_inicia_jogo():
    print("Bem-vindo ao jogo do NIM! Escolha:\n")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")

def vencedor(ganha_comp, ganha_usuario):
    if ganha_comp:
        return print("Fim do jogo! O computador ganhou!")
    elif ganha_usuario:
        return print("Fim do jogo! Você ganhou!")
def print_rest_peca(n):
    if n > 1:
        return print("Agora restam apenas", n ,"peças no tabuleiro.")
    elif n == 1:
        return print("Agora restam apenas uma peça no tabuleiro.")
    
def computador_escolhe_jogada(n, m):
    i = 1
    while i <= m:
        if (n - i) % (m + 1) == 0:
            return i
        i += 1
    return i - 1
def usuario_escolhe_jogada(n, m):
    jogada = int(input("Quantas peças você vai tirar? "))
    if jogada > 0 and jogada <= m and jogada <= n:
        return jogada
    else:
        while not(jogada > 0 and jogada <= m and jogada <= n):
            print("Oops! Jogada inválida! Tente de novo.")
            jogada = int(input("Quantas peças você vai tirar? "))
            if jogada > 0 and jogada <= m and jogada <= n:
                return jogada    
def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peça por jogada? "))
    comp_ganha = False
    usuario_ganhou = False
    if (n) % (m + 1) == 0:
        print("Voce começa!")
        while n > 0: ## Usuário começa
            valor_usuario = usuario_escolhe_jogada(n, m)
            n = n - valor_usuario
            if valor_usuario == 1:
                print("Você retirou uma peça.")
                print_rest_peca(n)
            else:
                print("Você retirou ", valor_usuario,"peças")
                print_rest_peca(n)
            if n == 0:
                usuario_ganhou = True
                break
            valor_computador = computador_escolhe_jogada(n, m)
            n = n - valor_computador
            if valor_computador == 1:
                print("Computador tirou uma peça.")
                print_rest_peca(n)
            else:
                print("Computador tirou ",valor_computador,"peças.")
                print_rest_peca(n)
            if n == 0:
                comp_ganha = True
        vencedor(comp_ganha, usuario_ganhou)    
    else:
        print("Computador começa!")
        while n > 0:
            valor_computador = computador_escolhe_jogada(n, m)
            n = n - valor_computador
            if valor_computador == 1:
                print("O computador tirou uma peça.")
                print_rest_peca(n)
            else:
                print("\nO computador tirou ",valor_computador,"peças.")
                print_rest_peca(n)
            if n == 0:
                comp_ganha = True
                break
            valor_usuario = usuario_escolhe_jogada(n, m)
            n = n - valor_usuario
            if valor_usuario == 1:
                print("Você retirou uma peça.")
                print_rest_peca(n)
            else:
                print("Você retirou ", valor_usuario,"peças")
                print_inicia_jogo(n)
            if n == 0:
                usuario_ganhou = True
        vencedor(comp_ganha, usuario_ganhou)
            
def campeonato():
    i = 1
    while i <= 3 :
        print("**** Rodada ", i , "****")
        partida()
        i += 1
    print("**** Final do campeonato! ****")
    print("\nPlacar: Você 0 X 3 Computador")
    
def main():
    print_inicia_jogo()
    jogar = 3
    while (jogar != 1 or jogar != 2):
        jogar = int(input())
        if jogar == 1:
            partida()
            estive_aqui = True
        elif jogar == 2:
            campeonato()
            estive_aqui = True
main()