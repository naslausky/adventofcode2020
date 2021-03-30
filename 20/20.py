class Tile:#Classe que representa uma peça do mapa
	def __init__(self, strings, ind):
		self.caracteres = strings
		self.indice = ind 

	def linhaSuperior(self):
		return self.caracteres[0]

	def linhaInferior(self):
		return self.caracteres[-1]

	def linhaEsquerda(self):
		return "".join([linha[0] for linha in self.caracteres])

	def linhaDireita(self):
		return "".join([linha[-1] for linha in self.caracteres])

	def obterLateraisDoTile(self):
		return [self.linhaSuperior(),self.linhaInferior(),self.linhaEsquerda(),self.linhaDireita()]

	def obterLateraisEspelhadas(self):
		return ["".join(list(reversed(linha))) for linha in self.obterLateraisDoTile()]

	def obterTodasAsLaterais(self):
		return self.obterLateraisEspelhadas()+self.obterLateraisDoTile()

	def espelhar(self):#Método que espelha horizontalmente os caracteres do tile
		for indice, linha in enumerate(self.caracteres):
			self.caracteres[indice] = "".join(list(reversed(linha)))

	def rotacionar(self):#Método que rotaciona um tile no sentido anti-horário
		novosCaracteres = []
		for i in range(len(self.caracteres[0])):
			novaLinha = "".join([linha[-i-1] for linha in self.caracteres])
			novosCaracteres.append(novaLinha)
		self.caracteres = novosCaracteres
	def rotacionarAteEncaixar (self, aresta, topo=False): #Método que rotaciona até encaixar no topo ou na lateral esquerda.
		metodoDaArestaACombinar = self.linhaSuperior if topo else self.linhaEsquerda
		for _ in range(4):
			self.rotacionar()
			if metodoDaArestaACombinar() == aresta: #Encaixou
				return
		self.espelhar()
		for _ in range(4):
			self.rotacionar()
			if metodoDaArestaACombinar() == aresta: #Encaixou
				return
tiles = []
numeroTileAtual = 0
tileAtual = []
with open('input.txt') as file:
	for linha in file:
		if linha == '\n': #Chegou ao fim de uma tile
			tiles.append(Tile(tileAtual,numeroTileAtual))
			tileAtual = []
		else:
			if ':' in linha:
				numeroTileAtual= int(linha [5:-2])
			else:
				tileAtual.append(linha[:-1])
#Parte 1:
arestasDosTiles = {tile.indice:set(tile.obterTodasAsLaterais()) for tile in tiles}
multiplicacao = 1
for indiceTile,arestas in arestasDosTiles.items():
	numeroDeArestasCombinantes = 0
	arestasCombinantesDoTile=[]
	for aresta in arestas: #Verifica se tem outro tile com alguma aresta combinando:
		for indiceTile2,arestas2 in arestasDosTiles.items():
			if indiceTile2==indiceTile:
				continue
			if aresta in arestas2:
				numeroDeArestasCombinantes +=1
				ultimaAresta=aresta
				arestasCombinantesDoTile.append(aresta)
	if numeroDeArestasCombinantes == 4:
		multiplicacao*=indiceTile
		primeiroTile = indiceTile
		primeirasArestas = arestasCombinantesDoTile[:]
print(multiplicacao)

#Parte 2:
dicionarioTiles = {tile.indice:tile for tile in tiles}
tilesJaUsados = []

#O primeiro precisa ser rodado até saber a orientação correta. Por agora está bugado
#dicionarioTiles[primeiroTile].rotacionarAteEncaixar(ultimaAresta)
#dicionarioTiles[primeiroTile].espelhar()

dicionarioTiles[primeiroTile].rotacionar()

for tile in tiles:
	if tile.indice == primeiroTile:
		tilesJaUsados.append(tile.indice)
numeroDeTiles = int(len(tiles)**(1/2)) #O enunciado diz que é uma imagem quadrada
print(tilesJaUsados)
for linha in range (numeroDeTiles):
	for coluna in range((1 if linha==0 else 0), numeroDeTiles):
		arestaAEncaixar = dicionarioTiles[tilesJaUsados[-12]].linhaInferior() if coluna==0 else dicionarioTiles[tilesJaUsados[-1]].linhaDireita()
		if (linha==0 and coluna==1):
			print(arestaAEncaixar)
		for tile in tiles:
			if tile.indice not in tilesJaUsados:
				if arestaAEncaixar in tile.obterTodasAsLaterais(): #Tile correto.
					tilesJaUsados.append(tile.indice)
					tile.rotacionarAteEncaixar(arestaAEncaixar, (coluna==0))

print(tilesJaUsados)
