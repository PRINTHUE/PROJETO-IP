# -*- coding: utf-8 -*-

from GUI import *

def adicionarPecas(tabuleiro, numeroDeJogadores):

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
    print("1. Adicionei as peças dos jogadores no tabuleiro")
    return tabuleiro


def pegarProximaPosicao(linhaAtual, posicaoNaLinhaAtual, direcao, salto):
    if salto == True:
        quantidadeDeLinhasPraPular = 2
        
    else:
        quantidadeDeLinhasPraPular = 1

    #a linha aumentará ou diminuirá
    proximaLinha = int(linhaAtual)
    if direcao == "ul" or direcao == "ur":
        proximaLinha -= quantidadeDeLinhasPraPular
    elif direcao == "dl" or direcao == "dr":
        proximaLinha += quantidadeDeLinhasPraPular
    #caso contrário, permanece na mesma linha

    linhaAtual = int(linhaAtual)
    proximaLinha = int(proximaLinha)

    deslocamento = 0
    #se o movimento ocorrer totalmente em uma das três faixas da estrela, então o deslocamento de coluna é 0
    if (((linhaAtual>=1 and linhaAtual<=4) and (proximaLinha>=1 and proximaLinha<=4)) or   #movimento todo na 1a faixa
    ((linhaAtual>=14 and linhaAtual<=17) and (proximaLinha>=14 and proximaLinha<=17)) or   #movimento todo na 4a faixa
    ((linhaAtual>=5 and linhaAtual<=13) and (proximaLinha>=5 and proximaLinha<=13))):      #movimento todo na 2a e 3a faixas
        deslocamento = 0  #não precisava, mas estou apenas reforcando

    elif (((linhaAtual>=1 and linhaAtual<=4) and (proximaLinha>=5 and proximaLinha<=9)) or #movimento da 1a pra 2a faixa
    ((linhaAtual>=14 and linhaAtual<=17) and (proximaLinha>=9 and proximaLinha<=13))):     #movimento da 4a pra 3a faixa
        deslocamento = 4

    elif (((linhaAtual>=5 and linhaAtual<=9) and (proximaLinha>=1 and proximaLinha<=4)) or #movimento da 2a pra 1a faixa
    ((linhaAtual>=9 and linhaAtual<=13) and (proximaLinha>=14 and proximaLinha<=17))):     #movimento da 3a pra 4a faixa
        deslocamento = -4

    posicaoNaProximaLinha = int(posicaoNaLinhaAtual)
    if direcao=="ul":
        if (((linhaAtual>=1 and linhaAtual<=4) and (proximaLinha>=1 and proximaLinha<=4)) or   #movimento todo na 1a faixa
        ((linhaAtual>=9 and linhaAtual<=13) and (proximaLinha>=9 and proximaLinha<=13)) or     #movimento todo na 3a faixa
        ((linhaAtual>=5 and linhaAtual<=6) and (proximaLinha>=3 and proximaLinha<=4))):        #movimento da faixa 2 para a faixa 1
            posicaoNaProximaLinha += deslocamento - quantidadeDeLinhasPraPular

            if linhaAtual == 6 and proximaLinha == 4:                                          #caso especial: movimento da 2a p 1a faixa
                posicaoNaProximaLinha += 1
        else:
            posicaoNaProximaLinha += deslocamento
            if linhaAtual == 14 and proximaLinha == 12:                                        #caso especial: movimento da 4a p 3a faixa
                posicaoNaProximaLinha -= 1

    elif direcao=="ur" :
        if (((linhaAtual>=5 and linhaAtual<=9) and (proximaLinha>=5 and proximaLinha<=9)) or   #movimento todo na 2a faixa
        ((linhaAtual>=14 and linhaAtual<=17) and (proximaLinha>=14 and proximaLinha<=17)) or   #movimento todo na 4a faixa
        ((linhaAtual>=14 and linhaAtual<=15) and (proximaLinha>=12 and proximaLinha<=13))):    #movimento inicia na 4a faixa e termina na 3a faixa
            posicaoNaProximaLinha += deslocamento + quantidadeDeLinhasPraPular

            if linhaAtual == 14 and proximaLinha == 12:                                        #caso especial: movimento da 4a p 3a faixa
                posicaoNaProximaLinha -= 1
        else:
            posicaoNaProximaLinha += deslocamento

            if linhaAtual == 6 and proximaLinha == 4:                                          #caso especial: movimento da 2a p 1a faixa
                posicaoNaProximaLinha += 1

    elif direcao == "dr" :
        if (((linhaAtual>=1 and linhaAtual<=4) and (proximaLinha>=1 and proximaLinha<=6)) or   #movimento todo na 1a faixa
        ((linhaAtual>=9 and linhaAtual<=13) and (proximaLinha>=9 and proximaLinha<=15)) or     #movimento todo na 3a faixa
        ((linhaAtual>=12 and linhaAtual<=13) and (proximaLinha>=14 and proximaLinha<=15))):    #movimento inicia na 4a faixa e termina na 3a faixa
            posicaoNaProximaLinha += deslocamento + quantidadeDeLinhasPraPular

            if ((linhaAtual == 4 and proximaLinha == 6) or                                     #caso especial: movimento da 1a p 2a faixa
            (linhaAtual == 12 and proximaLinha == 14)):                                        #caso especial: movimento da 3a p 4a faixa 
                posicaoNaProximaLinha -= 1

            elif(linhaAtual==13 and (proximaLinha>=14 and proximaLinha<=15)):                  #caso especial: movimento inicia na 3a faixa e termina na 4a faixa
                posicaoNaProximaLinha -= quantidadeDeLinhasPraPular
        else:
            posicaoNaProximaLinha += deslocamento 

    elif direcao=="dl" :
        if (((linhaAtual>=5 and linhaAtual<=9) and (proximaLinha>=5 and proximaLinha<=9)) or   #movimento todo na 2a faixa
        ((linhaAtual>=14 and linhaAtual<=17) and (proximaLinha>=14 and proximaLinha<=17)) or   #movimento todo na 4a faixa
        ((linhaAtual>=12 and linhaAtual<=13) and (proximaLinha>=14 and proximaLinha<=15))):    #movimento da faixa 3 para a faixa 4
            posicaoNaProximaLinha += deslocamento - quantidadeDeLinhasPraPular

            if linhaAtual == 12 and proximaLinha == 14:                                        #caso especial: movimento da 3a p 4a faixa
                posicaoNaProximaLinha += 1
        else:
            posicaoNaProximaLinha += deslocamento

            if linhaAtual == 4 and proximaLinha == 6:                                          #caso especial: movimento da 1a p 2a faixa
                posicaoNaProximaLinha -= 1
            
    elif direcao == "l":
        posicaoNaProximaLinha -= quantidadeDeLinhasPraPular
        
    else: #"r"
        posicaoNaProximaLinha += quantidadeDeLinhasPraPular
    print("2. Peguei a próxia posição do jogador no tabuleiro")
    print(int(proximaLinha),int(posicaoNaProximaLinha))
    return [proximaLinha,posicaoNaProximaLinha]
    
    

def validaString(entrada):
    tamanhoDaEntrada = len(entrada)

    if (tamanhoDaEntrada == 3):
        if entrada[0].isdigit() and entrada[1].isdigit():
            if entrada[2].isalpha():
                print("3.Validei sua String, ela é válida")
                return True

            else:
                print("Validei sua string, ela não é válida")
                return False

        else:
            print("3.Validei sua String, ela não é válida")
            return False
                                    
    elif (tamanhoDaEntrada > 3):
        if entrada[0].isdigit() and entrada[1].isdigit():
            for i in range(2,len(entrada[2:])+2):
                if entrada[i].isalpha() == False:
                    print("3.Validei sua String composta, ela não é válida")
                    return False
                    
                
        else:
            print("Validei sua String composta, ela não é válida")
            return False

    else:
        print("Validei sua String, ela não é válida")
        return False
        



def verificaLimites(entrada,tabuleiro):
    if int(entrada[0]) >= 1 and int(entrada[0]) <= len(tabuleiro):
        if int(entrada[1]) >= 1 and int(entrada[1]) <= len(tabuleiro[int(entrada[0])-1]):
            print("4.Verifiquei os limites do tabuleiro, vc está nos limites")
            return True

        else:
            print("4.Verifiquei os limites do tabuleiro, vc não está nos limites")
            return False

    else:
        print("4.Verifiquei os limites do tabuleiro, vc não está nos limites")
        return False


def verificaDirecao(entrada):
    if len(entrada) >= 3:
        
        if entrada[2] == "r" or entrada[2] == "l" or entrada[2] == "dr" or entrada[2] == "dl" or entrada[2] == "ur" or entrada[2] == "ul":
            print("5.Verifiquei seu comando de direção, está correto")
            return True

        else:
            print("5.Verifiquei seu comando de direção, está errado")
            return False
    else:
        print("5.Verifiquei seu comando de direção, está errado")
        return False

def verificarEspacoVazio(novaLinha,novaPosicao,tabuleiro):
    if tabuleiro[novaLinha-1][novaPosicao-1] == "O":
        print("6.Verifiquei se existe um espaço vazio na sua nova posição, existe")
        return True

    else:
        print("6.Verifiquei se existe um espaço vazio na sua nova posição, não existe")
        return False


'''
def entrada_linha_posicao():
    entrada = input("Movimento: ").split("-")
    linhaAtual = entrada[0]
    posicaoNaLinhaAtual = entrada[1]
    direcao = entrada[2]

    return [entrada,linhaAtual,posicaoNaLinhaAtual,direcao]
'''


def tentarMovimento(entrada,jogadorDaVez,jogadores,tabuleiro,salto=False):

        # Valida a entrada e se a peça existe no tabuleiro
        validaString(entrada)
        verificaDirecao(entrada)
        verificaLimites(entrada,tabuleiro)

        if validaString(entrada) == True and verificaDirecao(entrada) == True and verificaLimites(entrada,tabuleiro) == True:
    
        
            print("ValidaString: ",validaString(entrada))
            print("VerificaDireção: ",verificaDirecao(entrada))
            print("ValidaLimites: ",verificaLimites(entrada,tabuleiro))
                    
            linhaAtual = entrada[0]
            posicaoNaLinhaAtual = entrada[1]
            direcao = entrada[2]

            print("linhaAtual: ",linhaAtual)
            print("posiçãoNaLinhaAtual: ",posicaoNaLinhaAtual)
            print("direção: ",direcao)

            
            #mov simples
            if tabuleiro[int(linhaAtual)-1][int(posicaoNaLinhaAtual)-1] == jogadores[int(jogadorDaVez)][1]:
                posicaoSemSalto = pegarProximaPosicao(linhaAtual,posicaoNaLinhaAtual,direcao,salto=False)
                novaLinha = int(posicaoSemSalto[0])
                novaPosicao = int(posicaoSemSalto[1])

                auxiliarNovaLinha = posicaoSemSalto[0] #auxiliares para receber o valor sem ser inteiro
                auxiliarNovaPosicao = posicaoSemSalto[1]
            
                if verificaLimites([novaLinha,novaPosicao],tabuleiro) == True:  
                    if verificarEspacoVazio(novaLinha,novaPosicao,tabuleiro)== True:
                        linhaAnterior, posicaoAnterior = linhaAtual,posicaoNaLinhaAtual
                        print("7.Defini sua próxima posição sem salto")
                        return [novaLinha,novaPosicao]
                    #mov c salto
                    else:
                        salto=True
                        posicaoComSalto = pegarProximaPosicao(linhaAtual,posicaoNaLinhaAtual,direcao,salto)
                        novaLinha = posicaoComSalto[0]
                        novaPosicao = posicaoComSalto[1]

                        if verificaLimites([novaLinha,novaPosicao],tabuleiro) == True:  
                            if verificarEspacoVazio(novaLinha,novaPosicao,tabuleiro)== True:
                                if len(entrada) == 3:
                                    print("7.Defini sua próxima posição com salto")
                                    return [novaLinha,novaPosicao]

                                else:
                                    entrada[0] = auxiliarNovaLinha
                                    entrada[1] = auxiliarNovaPosicao
                                    del entrada[2]
                                    return tentarMovimento(entrada,jogadorDaVez,jogadores,tabuleiro,salto)

                            else:
                                return []

                else:
                    print("7.Não foi possível efetuar o movimento, você está saindo do tabuleiro")
                    return []

            else:
                print("7.Não foi possível efetuar o movimento, esta peça não é sua")
                return []

        else:
            print("7.Não foi possível efetuar o movimento")
            return []


def movimento(linhaAnterior,posicaoAnterior,posicaoFinal,jogadores,tabuleiro,jogadorDaVez):
    novaLinha = posicaoFinal[0]
    print("nova linha: ",novaLinha)
    novaPosicao = posicaoFinal[1]
    tabuleiro[int(novaLinha)-1][int(novaPosicao)-1] = jogadores[jogadorDaVez][1]
    tabuleiro[int(linhaAnterior)-1][int(posicaoAnterior)-1] = "O"

    print("8.Fiz seu movimento, na teoria")
    imprimirTabuleiro(tabuleiro)

def validaVencedores(numeroDeJogadores,jogadores,jogadorDaVez,tabuleiro):
    if numeroDeJogadores == 2:
        if jogadorDaVez == 1:
            contadorDePecas = 0
            for linha in range (4):
                for coluna in range (len(tabuleiro[linha])):
                    if tabuleiro[linha][coluna] == "B":
                        contadorDePecas += 1
                    if contadorDePecas == 10:
                        print('Jogador 2 venceu !!!!!!!!!!!!11')
                        return True
                    else:
                        return False

        else:
            contadorDePecas = 0
            for linha in range (13,17):
                for coluna in range (len(tabuleiro[linha])):
                    if tabuleiro[linha][coluna] == "A":
                        contadorDePecas += 1
                    if contadorDePecas == 10:
                        print('Jogador 1 venceu !!!!!!!!!!!11')
                        return True
                    else:
                        return False
    
            
                            
                

'''


        while (validaString(entrada) == False) or (verificaLimites(entrada,tabuleiro) == False):
            print('Ops! movimento inválido, tente novamente.\n')
            entrada_linha_posicao()

            validaString(entrada)
            verificaLimites(entrada,tabuleiro)
            linhaAtual = entrada[0]
            posicaoNaLinhaAtual = entrada[1]
            direcao = entrada[2]


        linhaAtual = entrada[0]
        posicaoNaLinhaAtual = entrada[1]            
        direcao = entrada[2]
        if tabuleiro[linhaAtual-1][posicaoNaLinhaAtual-1] == jogadores[jogadorDaVez][1]:
            novaLinha = pegarProximaPosicao(linhaAtual,posicaoNaLinhaAtual,direcao,salto=False)[0]
            novaPosicao = pegarProximaPosicao(linhaAtual,posicaoNaLinhaAtual,direcao,salto=False)[1]
            limite = pegarProximaPosicao(linhaAtual,posicaoNaLinhaAtual,direcao,salto=False)
            verificaLimites(limite)  


        while  (verificaLimites == False) or (validaString == False):
            print("Jogada Inválida!")
            entrada = input("Movimento: ").split("-")
            linhaAtual = entrada[0]
            posicaoNaLinhaAtual = entrada[1]
            direcao = entrada[2]

            limite = pegarProximaPosicao(linhaAtual,posicaoNaLinhaAtual,direcao,salto=False)
            validaString(entrada)
            verificaLimites(entrada,tabuleiro)
            novaLinha, novaPosicao = limite.split(",")


        vazio = verificarEspacoVazio(novaLinha,novaPosicao,tabuleiro)
        if vazio == True:
            tabuleiro[novaLinha-1][novaPosicao-1] == listaDoJogadores[jogada]
            tabuleiro[linhaAtual-1][posicaoNaLinhaAtual-1] == "O"

        else:
            while (vazio == False) and (validaString(entrada)) == False and (verificaLimites(entrada,tabuleiro) == False):
                entrada = input("Movimento: ").split("-")
                linhaAtual = entrada[0]
                posicaoNaLinhaAtual = entrada[1]
                direcao = entrada[2]
                validaString(entrada)
                verificaLimites(entrada,tabuleiro)


        return tabuleiro
        imprimirTabuleiro(tabuleiro)
        jogadorDaVez += 1
        #Se a variável jogador da vez for igual ao número de jogadores, então seu valor deverá ser zero 
        if (jogadorDaVez == numeroDeJogadores-1):
            jogadorDaVez = 0
'''





# Valida string  //
# split('-')   
# vericar se a peça está nos limites do tabuleiro //
# verificar se a peça é do jogador
# pegar proxima posicao (sem salto) 
# verificar se a proxima posicao esta vazia
# Caso o movimento não funcione
# pegar proxima posicao com salto
# verifica se a proxima posicao esta vazia, verificar se a posicao intermediaria nao esta vazia (caso aconteca, efetue o movimento)
# Caso o tamanho seja maior que 3, chamar tentarMovimento, tendo como parametro a proxima direcao
