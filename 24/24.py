#Desafio do dia 24/12/2020
#a)Receber uma lista de caminhos em uma matriz hexagonal, e calcular o estado de cada item.
#b)Receber regras de transição de cada item e aplicar esse conjunto de regras 100 vezes.
with open('input.txt') as file:
	linhas = file.read().splitlines()
	dicionarioTiles = {} #Dicionário que relaciona a coordenada de cada tile a um booleano (True=Face Preta).
	for linha in linhas: #Para cada linha, seguir as direções para chegar a coordenada destino
		coordenada = [0,0]
		caracterAnterior = ''
		for caracter in linha:
			if caracter == 'e': #E, SE ou NE
				if caracterAnterior:
					if caracterAnterior == 's': #SE
						if coordenada[1]%2:
							coordenada[0] += 1	
							coordenada[1] += 1	
						else:
							coordenada[1] += 1
					else: #NE
						if coordenada[1]%2:
							coordenada[1] += 1
						else:
							coordenada[0] -= 1
							coordenada[1] += 1
				else: #E
					coordenada[1] += 2
				caracterAnterior=''
			elif caracter == 's': #SE ou SW, depende do próximo
				caracterAnterior = caracter
			elif caracter == 'w':
				if caracterAnterior:
					if caracterAnterior == 's': #SW
						if coordenada[1]%2:
							coordenada[0] += 1	
							coordenada[1] -= 1	
						else:
							coordenada[1] -= 1
					else: #NW
						if coordenada[1]%2:
							coordenada[1] -= 1
						else:
							coordenada[0] -= 1
							coordenada[1] -= 1
				else: #W
					coordenada[1] -= 2
				caracterAnterior=''
			elif caracter == 'n': #NE ou NW, depende do próximo
				caracterAnterior = caracter
		coordenada = tuple(coordenada)
		if coordenada in dicionarioTiles: 
			dicionarioTiles[coordenada] = not dicionarioTiles[coordenada] #Vira o tile
		else: #Caso não esteja significa que está com a face branca para cima
			dicionarioTiles[coordenada] = True
def numeroTotalDeFacesPretas():
	return sum([valor for valor in dicionarioTiles.values()])
print("O número total de tiles com a face preta virada para cima é:", numeroTotalDeFacesPretas())
#Parte 2:
def expandirTilesEmTornoDosTilesPretos():#Função que adiciona ao dicionário as chaves em torno dos tiles pretos.
	tilesASeAdicionar = {}
	for coordenada, tile in dicionarioTiles.items():
		if tile: #Apenas em torno dos tiles com a face preta para cima
			for coordenadaX in range(coordenada[0]-2, coordenada[0]+3): #Provavelmente exagerei
				for coordenadaY in range(coordenada[1]-2,coordenada[1]+3):
					if (coordenadaX,coordenadaY) not in dicionarioTiles:
						tilesASeAdicionar[(coordenadaX,coordenadaY)] = False
	dicionarioTiles.update(tilesASeAdicionar)
def coordenadasDosTilesAoRedor(coordenadaX,coordenadaY): #Função que retorna uma tupla de coordenadas ao redor.
	if coordenadaY%2:
		coordenadasASeVerificar = ((0,-2),(0,-1),(0,1),(0,2),(1,1),(1,-1))
	else:
		coordenadasASeVerificar = ((0,-2),(-1,-1),(-1,1),(0,2),(0,1),(0,-1))
	return ((coordenadaX+coordenada[0],coordenadaY+coordenada[1]) for coordenada in coordenadasASeVerificar)
def numeroDeTilesPretosEmTornoDoTile(coordenadaX,coordenadaY):
	return sum([dicionarioTiles.get(coordenada,False) 
					for coordenada in coordenadasDosTilesAoRedor(coordenadaX,coordenadaY)])
for dia in range(100): #Realizar o procedimento por 100 dias.
	tilesAMudar = {}#Dicionário com as alterações do dia.
	expandirTilesEmTornoDosTilesPretos()
	for coordenada, tile in dicionarioTiles.items():
		numeroDeTilesPretoEmVolta = numeroDeTilesPretosEmTornoDoTile(*coordenada)
		if tile:
			if (numeroDeTilesPretoEmVolta == 0) or (numeroDeTilesPretoEmVolta >2):
				tilesAMudar[coordenada] = False
		else:
			if numeroDeTilesPretoEmVolta == 2:
				tilesAMudar[coordenada] = True
	dicionarioTiles.update(tilesAMudar)
print("O número total de tiles com a face preta virada para cima após 100 dias é:", numeroTotalDeFacesPretas())
