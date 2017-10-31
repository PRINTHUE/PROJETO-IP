from GUI import *
from LOGICA import *

numeroJogadores = menuInicial()
tabuleiro = criarTabuleiro()
tabuleiro = adicionarPecas(tabuleiro,numeroJogadores)                                                    

imprimirTabuleiro(tabuleiro)
print('\n\n\n')
