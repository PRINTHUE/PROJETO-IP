from GUI import *
from LOGICA import *

tabuleiro = criarTabuleiro()
numeroDeJogadores = totalDeJogadores()
tabuleiro = adicionarPecas(tabuleiro,numeroDeJogadores)                                                    
imprimirTabuleiro(tabuleiro)
jogadores = listaDeJogadores(numeroDeJogadores)

jogadorDaVez = 0
existeGanhadores = False

while existeGanhadores == False:
	for jogadorDaVez in range(numeroDeJogadores):
		print("Jogador da Vez: {}".format(jogadores[jogadorDaVez][0]))
		print("Peça: ",jogadores[jogadorDaVez][1])
		print("Quantidade de jogadas: {}".format(jogadores[jogadorDaVez][2]))

		entrada = input("Insira o seu movimento: ").split("-")
		posicaoFinal = tentarMovimento(entrada,jogadorDaVez,jogadores,tabuleiro,salto=False)

		while posicaoFinal == []:
			entrada = input("Ops, insira o seu movimento novamente: ").split("-")
			posicaoFinal = tentarMovimento(entrada,jogadorDaVez,jogadores,tabuleiro,salto=False)

		linhaAnterior = entrada[0]
		posicaoAnterior = entrada[1]
        
		movimento(linhaAnterior,posicaoAnterior,posicaoFinal,jogadores,tabuleiro,jogadorDaVez)
		jogadores[jogadorDaVez][2] += 1 


		jogadorDaVez += 1
		existeGanhadores = validaVencedores(numeroDeJogadores,jogadores,jogadorDaVez,tabuleiro)

	jogadorDaVez = 0
		
print('{} parabéns, você venceu!!!'.format(jogadores[jogadorDaVez][0]))
time.sleep(3)
limpaTela()
fimDeJogo()
