# -*- coding: utf-8 -*-

from GUI import *

def adicionarPecas(tabuleiro, numeroDeJogadores):
    tabuleiro = criarTabuleiro()
    nomeJogadores(numeroDeJogadores)
    
    
    if (numeroDeJogadores == 2):
        for linha in range(4):
            for coluna in range(linha+1):
                tabuleiro[linha][coluna] = 'A'

        for linha in range(4,0,-1):
            for coluna in range(linha):
                tabuleiro[17-linha][coluna] = 'B'

    elif (numeroDeJogadores == 3):
        x = 4
        for linha in range(4,8): # 4 5 6 7
            for coluna in range(x):  # 0 1 2 3
                tabuleiro[linha][coluna] = 'A'
            x -= 1

        x =- 4
        for linha in range(4,8):
            for coluna in range(x,0):
                tabuleiro[linha][coluna] = 'B'
            x += 1
            
        for linha in range(4,0,-1):
            for coluna in range(linha):
                tabuleiro[17-linha][coluna] = 'C'

    elif (numeroDeJogadores == 4):
        x = 4
        for linha in range(4,8): # 4 5 6 
            for coluna in range(x):
                tabuleiro[linha][coluna] = 'A'
            x -= 1

        x = -4
        for linha in range(4,8):
            for coluna in range(x,0):
                tabuleiro[linha][coluna] = 'B'
            x += 1

        x = 1
        for linha in range(9,13):
            for coluna in range(x):
                tabuleiro[linha][coluna] = 'C'
            x += 1

        x = -1
        for linha in range(9,13):
            for coluna in range(x,0):
                tabuleiro[linha][coluna] = 'D'
            x -= 1

    elif (numeroDeJogadores == 6):
        for linha in range(4):
            for coluna in range(linha+1):
                tabuleiro[linha][coluna] = 'A'

        x = 4
        for linha in range(4,8):
            for coluna in range(x):
                tabuleiro[linha][coluna] = 'B'
            x-= 1

        x = -4
        for linha in range(4,8):
            for coluna in range(x,0):
                tabuleiro[linha][coluna] = 'C'
            x += 1        

        x = 1
        for linha in range(9,13):
            for coluna in range(x):
                tabuleiro[linha][coluna] = 'D'
            x += 1

        x = -1
        for linha in range(9,13):
            for coluna in range(x,0):
                tabuleiro[linha][coluna] = 'E'
            x -= 1

        for linha in range(4,0,-1):
            for coluna in range(linha):
                tabuleiro[17-linha][coluna] = 'F'
    
    return tabuleiro
