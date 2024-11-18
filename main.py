'''
- **Função `criaTabuleiro`:** Cria um tabuleiro vazio para o jogo da velha representado por uma matriz 3x3.
- **Função `imprimeTabuleiro`:** Exibe o tabuleiro no console em um formato amigável.
- **Função `testeTerminal`:** Verifica se o jogo terminou (vitória de 'x', vitória de 'o', ou empate). Retorna:
  - `1` se 'o' venceu;
  - `3` se 'x' venceu;
  - `2` para empate;
  - `0` se o jogo ainda não terminou.
- **Funções `acaoMax` e `acaoMin`:** Implementam a lógica minimax para que a CPU jogue de forma ideal:
  - `acaoMax`: Determina o melhor movimento para 'x'.
  - `acaoMin`: Determina o melhor movimento para 'o'.
- **Função `principal`:** Controla o fluxo do jogo:
  - Permite diferentes modos de jogo: CPU vs. CPU, Jogador vs. CPU e Jogador vs. Jogador.
  - Alterna turnos entre os jogadores/CPU.
  - Determina o vencedor ou empate e pergunta se o jogador deseja continuar.
'''

import os

def criaTabuleiro():
    return [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def imprimeTabuleiro(tabuleiro):
    print('  1 2 3')
    for i in range(3):
        print('%d' % (i+1), *tabuleiro[i], '', sep='|')

def testeTerminal(tabuleiro):
    # Testa diagonal principal
    if tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][2]:
        if tabuleiro[0][0] == 'x':
            return 3
        elif tabuleiro[0][0] == 'o':
            return 1
    # Testa diagonal secundária
    if tabuleiro[2][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[0][2]:
        if tabuleiro[2][0] == 'x':
            return 3
        elif tabuleiro[2][0] == 'o':
            return 1
    # Testa linhas e colunas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] and tabuleiro[i][1] == tabuleiro[i][2]:
            if tabuleiro[i][0] == 'x':
                return 3
            elif tabuleiro[i][0] == 'o':
                return 1
        if tabuleiro[0][i] == tabuleiro[1][i] and tabuleiro[1][i] == tabuleiro[2][i]:
            if tabuleiro[0][i] == 'x':
                return 3
            elif tabuleiro[0][i] == 'o':
                return 1
    # Verifica empate
    empate = True
    for i in range(3):
        if ' ' in tabuleiro[i]:
            empate = False
    if empate:
        return 2
    return 0

def acaoMax(tabuleiro):
    terminal = testeTerminal(tabuleiro)
    if terminal:
        return [terminal, tabuleiro]
    acoes = []
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == ' ':
                copia = [list(tabuleiro[0]), list(tabuleiro[1]), list(tabuleiro[2])]
                copia[i][j] = 'x'
                acoes.append([0, copia])
    for i in range(len(acoes)):
        acoes[i][0] = acaoMin(acoes[i][1])[0]
    return max(acoes)

def acaoMin(tabuleiro):
    terminal = testeTerminal(tabuleiro)
    if terminal:
        return [terminal, tabuleiro]
    acoes = []
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == ' ':
                copia = [list(tabuleiro[0]), list(tabuleiro[1]), list(tabuleiro[2])]
                copia[i][j] = 'o'
                acoes.append([0, copia])
    for i in range(len(acoes)):
        acoes[i][0] = acaoMax(acoes[i][1])[0]
    return min(acoes)

def principal():
    cpuPrimeiro = True
    while True:
        print('1-CPU 1 x CPU 2\n2-Jogador x CPU\n3-Jogador 1 x Jogador 2')
        op = int(input('4-Sair\nOpção: '))
        vezCPU = True
        if op >= 1 and op <= 3:
            while True:
                tabuleiro = criaTabuleiro()
                os.system('cls' if os.name == 'nt' else 'clear')
                imprimeTabuleiro(tabuleiro)
                vezPrimeiro = True
                while not testeTerminal(tabuleiro):
                    if vezCPU and (op == 1 or op == 2):
                        if vezPrimeiro:
                            aux = acaoMax(tabuleiro)
                            tabuleiro = aux[1]
                        else:
                            aux = acaoMin(tabuleiro)
                            tabuleiro = aux[1]
                    else:
                        while True:
                            if vezPrimeiro and (op == 3 or not cpuPrimeiro):
                                print('Jogador [x]: ')
                                valor = 'x'
                            else:
                                print('Jogador [o]: ')
                                valor = 'o'
                            linha = int(input('linha: '))
                            coluna = int(input('coluna: '))
                            if linha > 0 and linha < 4 and coluna > 0 and coluna < 4:
                                if tabuleiro[linha-1][coluna-1] == ' ':
                                    tabuleiro[linha-1][coluna-1] = valor
                                    break
                    if op == 2:
                        vezCPU = not vezCPU
                    os.system('cls' if os.name == 'nt' else 'clear')
                    imprimeTabuleiro(tabuleiro)
                    vezPrimeiro = not vezPrimeiro
                if op == 2:
                    cpuPrimeiro = not cpuPrimeiro
                else:
                    cpuPrimeiro = True
                vezCPU = cpuPrimeiro

                resultado = testeTerminal(tabuleiro)
                if resultado == 1:
                    print('Vitória do [o]!')
                elif resultado == 3:
                    print('Vitória do [x]!')
                else:
                    print('Empate!')
                while True:
                    saida = input('Jogar novamente?[sim ou não] ')
                    saida = saida.lower()
                    if saida == 'sim' or saida == 'não':
                        break
                if saida == 'não':
                    break
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            return

# Executa o jogo
principal()

