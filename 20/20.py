tiles = {}
numeroTileAtual = 0
tileAtual = []
with open('input.txt') as file:
	for linha in file:
		if linha == '\n': #Chegou ao fim de uma tile
			tiles[numeroTileAtual] = tileAtual
			tileAtual = []
		else:
			if ':' in linha:
				numeroTileAtual= int(linha [5:-2])
			else:
				tileAtual.append(linha[:-1])

def obterLateraisDoTile(tile):
	linhaSuperior = tile[0]
	linhaInferior = tile[-1]
	linhaEsquerda = "".join([linha[0] for linha in tile])
	linhaDireita = "".join([linha[-1] for linha in tile])
	return [linhaSuperior,linhaInferior,linhaEsquerda,linhaDireita]

def obterLateraisEspelhadas(tile):
	return ["".join(list(reversed(linha))) for linha in obterLateraisDoTile(tile)]

def obterTodasAsLaterais(tile):
	return obterLateraisEspelhadas(tile)+obterLateraisDoTile(tile)

arestasDosTiles = {indice:set(obterTodasAsLaterais(tile)) for indice,tile in tiles.items()}
multiplicacao = 1
for indiceTile,arestas in arestasDosTiles.items():
	numeroDeArestasCombinantes = 0
	for aresta in arestas: #Verifica se tem outro tile com alguma aresta combinando:
		for indiceTile2,arestas2 in arestasDosTiles.items():
			if indiceTile2==indiceTile:
				continue
			if aresta in arestas2:
				numeroDeArestasCombinantes +=1
				ultimoLado = aresta
	if numeroDeArestasCombinantes == 4:
		multiplicacao*=indiceTile
		tileDoCanto = indiceTile
#Parte 2:
posicaoDosTiles = {tileDoCanto : (0,0)}
listaDosEspelhados =
resultadoTotal = []
arestasDosTiles = {indice:set(obterLateraisDoTile(tile)) for indice,tile in tiles.items()}
for linha in range(12):
	for coluna in range(12):
		if coluna == 0 and linha == 0:
			continue
		for indiceTile,arestas in arestasDosTiles.items():
			if ultimoLado in arestas:
				posicaoDosTiles[indiceTile] = (linha,coluna)
			elif ultimoLado in ["".join(list(reversed(linha))) for linha in arestas]:
				
				
for indiceTile,arestas in arestasDosTiles.items():
	numeroDeArestasCombinantes = 0
	for aresta in arestas: #Verifica se tem outro tile com alguma aresta combinando:
		for indiceTile2,arestas2 in arestasDosTiles.items():
			if indiceTile2==indiceTile:
				continue
			if aresta in arestas2:
				numeroDeArestasCombinantes +=1
	if numeroDeArestasCombinantes == 4:
		multiplicacao*=indiceTile
print(multiplicacao)
