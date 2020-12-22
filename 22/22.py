#Desafio do dia 22/12/2020
#a)Receber uma disposição de cartas para dois jogadores e dadas as regras de um jogo verificar a pontuação do vencedor.
#b) Modificar as regras um pouco para permitir jogos recursivos e recalcular a pontuação do vencedor.

with open('input.txt') as file:
	linhas = file.read().splitlines()
	for indice, linha in enumerate(linhas):
		if linha == '':
			baralhoJogador1 = linhas[1:indice]
			baralhoJogador1 = list(map(int,baralhoJogador1))
			baralhoJogador2 = linhas[indice+2:]
			baralhoJogador2 = list(map(int,baralhoJogador2))
			disposicaoOriginalDosBaralhos = (baralhoJogador1[:],baralhoJogador2[:]) #Salva para Parte 2.
while (baralhoJogador1 and baralhoJogador2): #Ambos os baralhos ainda possuem cartas.
	cartaJogador1, cartaJogador2 = baralhoJogador1[0], baralhoJogador2[0] #Saca uma carta de cada baralho.
	cartasDaRodada = [cartaJogador1, cartaJogador2]
	cartasDaRodada.sort(reverse=True) #Carta de maior valor fica no topo.
	baralhoJogador1, baralhoJogador2 = baralhoJogador1[1:], baralhoJogador2[1:] #Remove a carta sacada.
	baralhoVencedor = baralhoJogador1 if cartaJogador1>cartaJogador2 else baralhoJogador2 #Verifica o vencedor.
	baralhoVencedor.extend(cartasDaRodada)
def pontuacaoDoBaralho(baralho):
	return sum([(peso+1)*carta for peso,carta in enumerate(reversed(baralho))])
print("Pontuação do baralho do vencedor:", pontuacaoDoBaralho(baralhoJogador1+baralhoJogador2))

#Parte2:
def jogarCombateRecursivo(cartas1,cartas2): #Função que executa uma partida do jogo recursivo.
	arranjoDosRoundsAnteriores = set() #Lista de tuplas que representa as disposições de cartas já ocorridas.
	while (True):
		arranjoDeCartasDesseTurno = (tuple(cartas1), tuple(cartas2)) #Adicionar na lista ao final do round.
		if arranjoDeCartasDesseTurno in arranjoDosRoundsAnteriores:
			return 1, cartas1 #Caso essa combinação já tenha acontecido, vitória do jogador 1.
		cartaJogador1, cartaJogador2 = cartas1[0], cartas2[0] 
		cartas1, cartas2 = cartas1[1:], cartas2[1:] 
		if (len(cartas1)>=cartaJogador1 and len(cartas2)>=cartaJogador2): #O suficiente para um sub-jogo.
			vencedor, _ = jogarCombateRecursivo(cartas1[:cartaJogador1],cartas2[:cartaJogador2])
			if vencedor == 1:
				cartas1.extend([cartaJogador1,cartaJogador2])
			else:
				cartas2.extend([cartaJogador2,cartaJogador1])
		else: #Não tem cartas suficientes para um sub-jogo. Vence quem tem a maior carta.
			if cartaJogador1>cartaJogador2:
				cartas1.extend([cartaJogador1,cartaJogador2])
			else:
				cartas2.extend([cartaJogador2,cartaJogador1])
		arranjoDosRoundsAnteriores.add(arranjoDeCartasDesseTurno)
		if not cartas1: #Jogador 2 venceu
			return 2, cartas2 #Precisa retornar as cartas para contagem dos pontos ao final.
		if not cartas2: #Jogador 1 venceu
			return 1, cartas1
_, baralhoVencedor = jogarCombateRecursivo(*disposicaoOriginalDosBaralhos)
print("Pontuação do baralho do vencedor no jogo recursivo:",pontuacaoDoBaralho(baralhoVencedor))
