from GUI import *
from LOGICA import *

tabuleiro = criarTabuleiro()
numeroDeJogadores = totalDeJogadores()
tabuleiro = adicionarPecas(tabuleiro,numeroDeJogadores)                                                    
imprimirTabuleiro(tabuleiro)

entrada = input("")
jogadorDaVez = 0

jogadores = listaDeJogadores(numeroDeJogadores) 
existeGanhadores = False

while existeGanhadores == False:
	for jogadorDaVez in range(numeroDeJogadores):
		entrada = pedirMovimento(jogadores,jogadorDaVez)

		posicaoFinal = tentarMovimento(numeroDeJogadores,jogadorDaVez,jogadores,tabuleiro,salto=False)
		

	
print('\n\n\n') 