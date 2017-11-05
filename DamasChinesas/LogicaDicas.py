# -*- coding: utf-8 -*-

def pegarProximaPosicao(linhaAtual, posicaoNaLinhaAtual, direcao, salto):
    if salto == True:
        quantidadeDeLinhasPraPular=2
    else:
        quantidadeDeLinhasPraPular=1

    #a linha aumentará ou diminuirá
    proximaLinha = linhaAtual
    if direcao == "ul" or direcao == "ur":
        #como deverá ser computada a próxima linha?

    deslocamento = 0
    #se o movimento ocorrer totalmente em uma das três faixas da estrela, então o deslocamento de coluna é 0
    if (((linhaAtual>=1 and linhaAtual<=4) and (proximaLinha>=1 and proximaLinha<=4)) or   #movimento todo na 1a faixa
    ((linhaAtual>=14 and linhaAtual<=17) and (proximaLinha>=14 and proximaLinha<=17)) or   #movimento todo na 4a faixa
    ((linhaAtual>=5 and linhaAtual<=13) and (proximaLinha>=5 and proximaLinha<=13))):      #movimento todo na 2a e 3a faixas
        deslocamento = 0  #não precisava, mas estou apenas reforcando
    #qual é o deslocamento quando:
        #1 - movimento for da (1a pra 2a faixa) ou da (4a pra 3a faixa)
        #2 - movimento for da (2a pra 1a faixa) ou da (3a pra 4a faixa)

    #aqui tem muitos casos e é a parte complicada...
    #primeira coisa a fazer é ajustar a posicaoNaProximaLinha para posicaoNaLinhaAtual, pois a posicao na proxima linha
    #será calculada a partir da posicaoNaLinhaAtual
    posicaoNaProximaLinha = posicaoNaLinhaAtual     
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
    #os casos que faltam que você identifique padrão são:
        #quando for "ur":
                #1 - movimento (todo na 2a faixa) ou (todo na 4a faixa) ou (inicia na 4a faixa e termina na 3a faixa)
                #caso especial: movimento da 4a p 3a faixa (linha 14 para linha 12)
                #caso especial: movimento da 2a p 1a faixa (linha 6 para linha 4)
        #quando for "dr":
                #1 - movimento (todo na 1a faixa) ou (todo na 3a faixa) ou (inicia na 4a faixa e termina na 3a faixa)
                #caso especial: movimento da 1a p 2a faixa (linha 4 para linha 6) ou movimento da 3a p 4a faixa 
                #caso especial: movimento inicia na 3a faixa e termina na 4a faixa
    #identificar padrões de modo semelhante para dr e dl
            
    elif direcao == "l":
        posicaoNaProximaLinha -= quantidadeDeLinhasPraPular
    else: #"r"
        posicaoNaProximaLinha += quantidadeDeLinhasPraPular

    return [proximaLinha, posicaoNaProximaLinha]
    



    
    
    
