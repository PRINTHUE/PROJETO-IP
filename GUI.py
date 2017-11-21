# -*- coding: utf-8 -*-
import time

def limpaTela():
    print('\n'*50)
    

def validaNumeroDeJogadores(quantidade):
    if quantidade.isdigit():
        if int(quantidade) > 1 and int(quantidade) <= 6 and int(quantidade) != 5:
            return True

        else:
            return False

    else:
        return False


def cabecalho():
    print('$'*137)
    print('$'*137)
    print('$'*137)
    print('$'*137)
    print('$'*137)
    print('{} {:^65} {}'.format('$'*32,'D   A   M   A   S        C   H   I   N   E   S   A   S','$'*38))
    print('$'*137)
    print('$'*137)
    print('$'*137)
    print('$'*137)
    print('$'*137)
    print('$'*137)
    print('\n\n\n')

def totalDeJogadores():
    totalDeJogadores = input("Insira o Nº de jogadores: ")
    verificacao = validaNumeroDeJogadores(totalDeJogadores)

    while (verificacao == False):
        print("Quantidade Inválida, insira novamente\n")
        totalDeJogadores = input("Nº de jogadores: ")
        print("")
        verificacao = validaNumeroDeJogadores(totalDeJogadores)

    return int(totalDeJogadores)


def menuInicial():
    cabecalho()
    tabuleiro = criarTabuleiro()
    imprimirTabuleiro(tabuleiro)
    print("\n")

    quantidadeDeJogadores = numeroDeJogadores()
    informacoes = jogadores(quantidadeDeJogadores)


def listaDeJogadores(numeroDeJogadores):
    ID_JOGADORES = []
    pecas = ["A","B","C","D","E","F"]


    for jogador in range(numeroDeJogadores):
        nome = input('Jogador {}: '.format(jogador + 1))
        print("")
        ID_JOGADORES += [[nome,pecas[jogador],0]] 


    return ID_JOGADORES


def criarTabuleiro():
    Tabuleiro = []

    for linha in range(4): 
        Tabuleiro.append([])
        for coluna in range(linha+1):
            Tabuleiro[linha].append("O")  #0 1 2 3

    for linha in range(13,9,-1): #13 12 11 10
        Tabuleiro.append([])
        for coluna in range(linha):
            Tabuleiro[17-linha].append("O")  #4 5 6 7

    for linha in range(9,14): #9 10 11 12 13
        Tabuleiro.append([])
        for coluna in range(linha):
            Tabuleiro[linha-1].append("O")  #8 9 10 11 12

    for linha in range(4,0,-1):  #4 3 2 1
        Tabuleiro.append([])
        for coluna in range(linha):
            Tabuleiro[17-linha].append("O")  #13 14 15 16
                              
    return Tabuleiro


def imprimirLinhaComEspaco(tabuleiro,linha, espaco):
    tamanhoDoTabuleiro = len(tabuleiro[linha])
    espacamento = " " * espaco
    linhas = ""
    
    for i in range(tamanhoDoTabuleiro):
       linhas += tabuleiro[linha][i]
       linhas += " "
       
    print(espacamento+linhas)


def imprimirTabuleiro(tabuleiro):
    LINHA = 0   

    for espaco in range(13,9,-1): #13 12 11 10
        print('{:>47}'.format(LINHA+1),end='')
        imprimirLinhaComEspaco(tabuleiro,LINHA,espaco)
        LINHA += 1

    for espaco in range(1,6): #1 2 3 5 5
        print('{:>47}'.format(LINHA+1),end='')
        imprimirLinhaComEspaco(tabuleiro,LINHA,espaco)
        LINHA += 1

    for espaco in range(4,0,-1): #4 3 2 1
        print('{:>47}'.format(LINHA+1),end='')
        imprimirLinhaComEspaco(tabuleiro,LINHA,espaco)
        LINHA += 1

    for espaco in range(10,14): #10 11 12 13
        print('{:>47}'.format(LINHA+1),end='')
        imprimirLinhaComEspaco(tabuleiro,LINHA,espaco)
        LINHA += 1



def pedirMovimento(jogadores,jogDaVez):
    print("Jogador da Vez: {}".format(jogadores[jogDaVez][0]))
    return input("Insira seu movimento: ").split("-")
