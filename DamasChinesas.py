from GUI import *
from LOGICA import *

tabuleiro = criarTabuleiro()
numeroDeJogadores = totalDeJogadores()
tabuleiro = adicionarPecas(tabuleiro,numeroDeJogadores)                                                    
imprimirTabuleiro(tabuleiro)
jogadorDaVez = 0

jogadores = listaDeJogadores(numeroDeJogadores) 
existeGanhadores = False

while existeGanhadores == False:
    for jogadorDaVez in range(numeroDeJogadores):
        print("Jogador da Vez: {}".format(jogadores[jogadorDaVez][0]))
        print("Peça: ",jogadores[jogadorDaVez][1])
        entrada = input("Insira o seu movimento: ").split("-")


        posicaoFinal = tentarMovimento(entrada,jogadorDaVez,jogadores,tabuleiro,salto=False)
        print("posição final: ",posicaoFinal)

        while posicaoFinal == []:
            entrada = input("Movimento inválido, insira o seu movimento novamente: ").split("-")
            posicaoFinal = tentarMovimento(entrada,jogadorDaVez,jogadores,tabuleiro,salto=False)

        linhaAnterior = entrada[0]
        posicaoAnterior = entrada[1]
        print("linha anterior:",linhaAnterior)
        print("posicao anterior:",posicaoAnterior)
        
        #movimento(linhaAnterior,posicaoAnterior,posicaoFinal,jogadores,tabuleiro)
        movimento(linhaAnterior,posicaoAnterior,posicaoFinal,jogadores,tabuleiro,jogadorDaVez)
        

        existeGanhadores = validaVencedores(numeroDeJogadores,jogadores,jogadorDaVez,tabuleiro)
         
        #movimento(posicaoFinal)
        
        jogadorDaVez += 1

jogadorDaVez = 0	


print('\n\n\n') 
