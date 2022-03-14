########## Função principal ##########

def main():
    print(f'Bem-vindo ao jogo do NIM! Escolha:')
    print(f'1 - para jogar uma partida isolada')
    print(f'2 - para jogar um campeonato ')
    print()

    tipo_partida = int(input(f'Digite a opção desejada: '))

    if tipo_partida == 2:
        print()
        print(f'Você escolheu um campeonato!')
        print()
        campeonato()
    else:
        if tipo_partida == 1:
            print()
            partida()


########## Funções auxiliares do programa ##########

def computador_escolhe_jogada(n, m):
    computador_remove = 1

    while computador_remove != m:
        if (n - computador_remove) % (m+1) == 0:
            return computador_remove
        else:
            computador_remove += 1
    return computador_remove

def usuario_escolhe_jogada(n, m):
    jogada_valida = False

    while not jogada_valida:
        jogador_remove = int(input('Quantas peças você vai tirar? '))
        if jogador_remove > m or jogador_remove < 1:
            print()
            print(f'Jogada inválida! Tente de novo.')
            print()
        else:
            jogada_valida = True
    return jogador_remove

def campeonato():
    rodada = 1
    while rodada <= 3:
        print()
        print(f'********** Rodada {rodada} **********')
        print()
        partida()
        rodada += 1
    print()
    print(f'Placar: Você 0 X 3 Computador')


def partida():
    n = int(input(f'Quantas peças? '))
    m = int(input(f'Limite de peças por jogada? '))

    vez_computador= False

    if n % (m+1) == 0:
        print()
        print(f'Voce começa!')
    else:
        print()
        print(f'Computador começa!')
        vez_computador = True

    while n > 0:
        if vez_computador:
            computador_remove = computador_escolhe_jogada(n, m)
            n = n - computador_remove
            if computador_remove == 1:
                print()
                print(f'O computador tirou uma peça')
            else:
                print()
                print(f'O computador tirou {computador_remove} peças')

            vez_computador = False
        else:
            jogador_remove = usuario_escolhe_jogada(n, m)
            n = n - jogador_remove
            if jogador_remove == 1:
                print()
                print(f'Você tirou uma peça')
            else:
                print()
                print(f'Você tirou {jogador_remove} peças')
            vez_computador = True
        if n == 1:
            print(f'Agora resta apenas uma peça no tabuleiro.')
            print()
        else:
            if n != 0:
                print(f'Agora restam {n} peças no tabuleiro.')
                print()

    print(f'Fim do jogo! O computador ganhou!')
    
    
########## Execução do programa ##########
    
if __name__ == "__main__":
    main()