#Desafio do dia 20/12/2020
#a) Receber vários segmentos de um mapa. 
# Os segmentos são adjuntos a outros por bordas iguais. Descobrir quais os Ids segmentos das bordas. 
#b) Formar o mapa e contar quantas vezes um padrão informado ocorre.
import re
class Tile:#Classe que representa uma peça do mapa.
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

	def espelhar(self):#Método que espelha horizontalmente os caracteres do tile.
		for indice, linha in enumerate(self.caracteres):
			self.caracteres[indice] = "".join(list(reversed(linha)))

	def rotacionar(self):#Método que rotaciona um tile no sentido anti-horário.
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

	def rotacionarParaPrimeiraPosicao(self, arestasDosTiles): #O primeiro tile, do canto superior esquerdo, precisa estar com os lados sem combinações virados para cima e para esquerda.
		for _ in range(4):
			achou = True
			for indiceTile2, arestas2 in arestasDosTiles.items():
				if indiceTile2 == primeiroTile:
					continue
				if self.linhaSuperior() in arestas2:
					achou = False
				if self.linhaEsquerda() in arestas2:
					achou = False
			if achou:
				break
			else:
				self.rotacionar()
		if not achou:
			dicionarioTiles[primeiroTile].espelhar()
			for _ in range(4):
				achou = True
				for indiceTile2, arestas2 in arestasDosTiles.items():
					if indiceTile2 == primeiroTile:
						continue
					if self.linhaSuperior() in arestas2:
						achou = False
					if self.linhaEsquerda() in arestas2:
						achou = False
				if achou:
					break
				else:
					self.rotacionar()

	def removerBordas(self):
		self.caracteres = [string[1:-1] for string in self.caracteres[1:-1]]

	def imprimir(self):
		for linha in self.caracteres:
			print(linha)

	def contabilizarMonstros(self, padraoMonstroMarinho): #Método que contabiliza quantas vezes o padrão aparece na imagem. Espero que não tenha monstros sobrepostos :)
		alturaMonstro = len(padraoMonstroMarinho)
		larguraMonstro = len(padraoMonstroMarinho[0])
		alturaImagem = len(self.caracteres)
		larguraImagem = len(self.linhaSuperior())
		numeroDeMonstros = 0
		for indiceLinha in range(alturaImagem - alturaMonstro + 1):
			for indiceColuna in range (larguraImagem - larguraMonstro + 1):
				linhaSuperior = self.caracteres[indiceLinha][indiceColuna:indiceColuna+larguraMonstro]
				linhaDoMeio = self.caracteres[indiceLinha+1][indiceColuna:indiceColuna+larguraMonstro]
				linhaInferior = self.caracteres[indiceLinha+2][indiceColuna:indiceColuna+larguraMonstro]
				if (re.match(padraoMonstroMarinho[0], linhaSuperior) and
					re.match(padraoMonstroMarinho[1], linhaDoMeio) and
					re.match(padraoMonstroMarinho[2],linhaInferior)):
						numeroDeMonstros+=1
		return numeroDeMonstros

	def rotacionarAteEncontrarMonstros(self, padraoMonstroMarinho): #Método que vai rodando e espelhando até achar a orientação que retorna monstros marinhos. 
		for _ in range(4):
			if self.contabilizarMonstros(padraoMonstroMarinho):
				break
			self.rotacionar()
		if not self.contabilizarMonstros(padraoMonstroMarinho):
			self.espelhar()
			for _ in range(4):
				if self.contabilizarMonstros(padraoMonstroMarinho):
					break
				self.rotacionar()
		return self.contabilizarMonstros(padraoMonstroMarinho)

	def contabilizarTralhas(self):
		return sum([x.count('#') for x in self.caracteres])

tiles = []
numeroTileAtual = 0
tileAtual = []
with open('input.txt') as file:
	for linha in file:
		if linha == '\n': #Chegou ao fim de uma tile.
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
print('O produto dos IDs dos tiles dos cantos é:', multiplicacao)

#Parte 2:
dicionarioTiles = {tile.indice:tile for tile in tiles}
tilesJaUsados = []
dicionarioTiles[primeiroTile].rotacionarParaPrimeiraPosicao(arestasDosTiles)

#Vai juntando os tiles para descobrir a posição de cada um. Anota os ids em uma tilesJaUsados.
tilesJaUsados.append(primeiroTile)
numeroDeTiles = int(len(tiles)**(1/2)) #O enunciado diz que é uma imagem quadrada.
for linha in range (numeroDeTiles):
	for coluna in range((1 if linha==0 else 0), numeroDeTiles):
		arestaAEncaixar = dicionarioTiles[tilesJaUsados[-12]].linhaInferior() if coluna==0 else dicionarioTiles[tilesJaUsados[-1]].linhaDireita()
		for tile in tiles:
			if tile.indice not in tilesJaUsados:
				if arestaAEncaixar in tile.obterTodasAsLaterais(): #Tile correto.
					tilesJaUsados.append(tile.indice)
					tile.rotacionarAteEncaixar(arestaAEncaixar, (coluna==0))

#Forma uma imagem final sem as bordas de cada tile:
[t.removerBordas() for t in tiles]
imagemFinal = []
for indiceImagem in range (numeroDeTiles):
	linhasASeremAdicionadas = [
				''.join([dicionarioTiles[i].caracteres[indiceLinha]  
					for i in tilesJaUsados[indiceImagem*12 : ((indiceImagem+1)*12)]]) 
					for indiceLinha in range(8)]
	imagemFinal.extend(linhasASeremAdicionadas)
tileFinal = Tile(imagemFinal,0) #Cria um tile da imagem final pra poder reaproveitar os métodos.

padraoMonstroMarinho = ['..................#.',
			'#....##....##....###',
			'.#..#..#..#..#..#...']
numeroDeMonstros = tileFinal.rotacionarAteEncontrarMonstros(padraoMonstroMarinho)
numeroDeTralhasEmCadaMonstro = sum([x.count('#') for x in padraoMonstroMarinho])
numeroDeTralhasNaImagemFinal = tileFinal.contabilizarTralhas() 
print('Número de tralhas que não fazem parte de um monstro:', numeroDeTralhasNaImagemFinal - (numeroDeTralhasEmCadaMonstro*numeroDeMonstros))
