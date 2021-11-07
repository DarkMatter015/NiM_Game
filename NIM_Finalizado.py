# Partida em Campeonato
def campeonato():
        camp= 3
        rod= 0
        player= 0
        comput= 0
        while camp > 0:
            camp-=1
            rod += 1
            print(f'*** Rodada {rod} ***')
            
            r= partida()
            if r == 0:
                comput+=1
            elif r == 1:
                player+=1
        if comput > player:
            print('Fim de Jogo. Computador ganhou!')
        elif player > comput:
            print('Fim de Jogo. Jogador ganhou!')
        print('*** Final do Campeonato ***')
        print(f'Placar: Você {player} X {comput} Computador')
                
# Computador Escolhendo Jogada
def computador_escolhe_jogada(n, m):
    if n <= m:
        # Retira todas as peças e ganha o jogo:
        return n
    else:
        # Verifica se é possível deixar uma quantia múltipla de m+1:
        quantia = n % (m + 1)
        if quantia > 0:
            return quantia
        # Não é, então tire m peças:
        return m

# Usuário Escolhendo Jogada 
def usuario_escolhe_jogada(n, m):
    pc= int(input('Quantas peças você vai tirar? '))
    while pc > m or pc > n or pc <= 0:
        print(f'[ERRO] Tente novamente.')
        pc= int(input('Quantas peças você vai tirar? '))
    
    return pc

# Sistema de Troca de Jogador
def Rodar(n, m):
    # Jogador começa!
    if n % (m+1) == 0:
        print('Você começa!')

        while n > 0:   
            u=usuario_escolhe_jogada(n, m)
            n-=u
            if u == 1:
                print(f'Você tirou uma peça.')
            elif u > 1:
                print(f'Você tirou {u} peças.')
            if n > 1:
                print(f'Agora restam {n} peças no tabuleiro.')
            elif n == 1:
                print(f'Agora resta apenas uma peça no tabuleiro.')
            if n==0:
                print('Usuário venceu!')
                return 1
            c= computador_escolhe_jogada(n, m)
            n-=c

            if c == 1:
                print(f'Computador tirou uma peça.')
            elif c > 1:
                print(f'Computador tirou {c} peças.')
            if n > 1:
                print(f'Agora restam {n} peças no tabuleiro.')
            elif n == 1:
                print(f'Agora resta apenas uma peça no tabuleiro.')

            if n==0:
                print('Computador venceu!')
                return 0

    # computador Começa
    else:
        print('computador começa!')

        while n > 0:

            c=computador_escolhe_jogada(n, m)
            n-= c
            if c == 1:
                print(f'Computador tirou uma peça.')
            elif c > 1:
                print(f'Computador tirou {c} peças.')
            if n > 1:
                print(f'Agora restam {n} peças no tabuleiro.')
            elif n == 1:
                print(f'Agora resta apenas uma peça no tabuleiro.')

            if n==0:
                print('Computador venceu!')
                return 0

            u=usuario_escolhe_jogada(n, m)
            n-=u
            if u == 1:
                print(f'Você tirou uma peça.')
            elif u > 1:
                print(f'Você tirou {u} peças.')
            if n > 1:
                print(f'Agora restam {n} peças no tabuleiro.')
            elif n == 1:
                print(f'Agora resta apenas uma peça no tabuleiro.')

            if n==0:
                print('Usuário venceu!')
                return 1

# Escolhendo Parâmetros
def partida():
    n= int(input('Quantas peças? '))
    while n <= 0:
        n= int(input('[ERRO TENTE NOVAMENTE]\nQuantas peças? '))
    m= int(input('Limite de peças por jogada? '))
    while m > n or m <= 0:
        m= int(input('[ERRO!TENTE NOVAMENTE]\nLimite de peças por jogada? '))
    
    # Retorna Placar
    r= Rodar(n, m)
    if r == 0:
        return 0
    elif r == 1:
        return 1

# Partida Principal
def main():
    a=0
    print('Bem vindo ao Jogo do NIM! Escolha:')
    pchoice= int(input('1- para jogar partida isolada\n2- para jogar campeonato '))
    if pchoice == 1:
        print('Partida isolada')
        a= 1
    elif pchoice == 2:
        print('Campeonato')
        a= 2
    # Partida Isolada
    if a == 1:
        partida()
    # Campeonato
    elif a == 2:
        campeonato()
# Chamada de Função
main() 