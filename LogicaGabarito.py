# -*- coding: utf-8 -*-

def pegarProximaPosicao(linhaAtual, posicaoNaLinhaAtual, direcao, salto):
    if salto == True:
        quantidadeDeLinhasPraPular=2
    else:
        quantidadeDeLinhasPraPular=1

    #a linha aumentará ou diminuirá
    proximaLinha = linhaAtual
    if direcao == "ul" or direcao == "ur":
        proximaLinha -= quantidadeDeLinhasPraPular
    elif direcao == "dl" or direcao == "dr":
        proximaLinha += quantidadeDeLinhasPraPular
    #caso contrário, permanece na mesma linha

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

    posicaoNaProximaLinha = posicaoNaLinhaAtual
    if direcao == "ul":
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
    elif direcao == "ur" :
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
    elif direcao == "dl" :
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

    return [proximaLinha, posicaoNaProximaLinha]
    



























    
