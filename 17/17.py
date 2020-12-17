#Desafio do dia 17/12/2020
#a)Receber uma matriz de caracteres representando um plano dentro de um espaço tridimensional N3.
#  Aplicar regras de transição 6 vezes e calcular o estado final.
#b)Idem porém para um espaço em 4 dimensões.

with open('input.txt') as file:
	linhas = file.read().splitlines()
	grid = {} #Dicionário que vai representar o espaço da seguinte forma: {(x,y,z):True, ...}
	grid4d = {} #Idem porém para 4 dimensões
	for indiceLinha, linha in enumerate(linhas):
		for indiceColuna, caracter in enumerate(linha):
			grid[(indiceLinha,indiceColuna,0)] = True if caracter == "#" else False
			grid4d[(indiceLinha,indiceColuna,0,0)] = True if caracter == "#" else False

def expandirGridEmTornoDosAtivos(): #Função que adiciona ao grid os elementos ao redor de todo elemento ativo.
	itensASeAdicionar = {}
	for coordenada, estado in grid.items():
		for coordenadaX in range(coordenada[0]-1,coordenada[0]+2):
			for coordenadaY in range(coordenada[1]-1,coordenada[1]+2):
				for coordenadaZ in range(coordenada[2]-1,coordenada[2]+2):
					coordenadaASeVerificar = (coordenadaX,coordenadaY,coordenadaZ)
					if coordenadaASeVerificar not in grid and estado: #Verificar apenas dos ativos
						itensASeAdicionar[coordenadaASeVerificar] = False
	grid.update(itensASeAdicionar)

for numeroCiclo in range(6): #Executar a transição 6 vezes
	expandirGridEmTornoDosAtivos() #Garantir que estamos verificando os cubos mais externos.
	gridAposIteracao = {} #Armazena as alterações desse ciclo. (Todos os cubos alteram simultaneamente.)
	for coordenada, estado in grid.items():
		numeroDeCubosAtivosEmVolta = 0
		for coordenadaX in range(coordenada[0]-1,coordenada[0]+2):
			for coordenadaY in range(coordenada[1]-1,coordenada[1]+2):
				for coordenadaZ in range(coordenada[2]-1,coordenada[2]+2):
					coordenadaASeVerificar = (coordenadaX,coordenadaY,coordenadaZ)
					if coordenadaASeVerificar in grid and coordenadaASeVerificar!=coordenada:
						numeroDeCubosAtivosEmVolta += grid[coordenadaASeVerificar] #True é avaliado para 1.
		if estado == True:
			if numeroDeCubosAtivosEmVolta != 2 and numeroDeCubosAtivosEmVolta != 3:
				gridAposIteracao[coordenada] = False
		else:
			if numeroDeCubosAtivosEmVolta == 3:
				gridAposIteracao[coordenada] = True
	grid.update(gridAposIteracao)
numeroDeCubosAtivos = sum(grid.values())
print('[3D] Número de cubos ativos após 6 ciclos:', numeroDeCubosAtivos)

#Parte 2:
def expandirGridEmTornoDosAtivos4d(): #Idem porém em 4 dimensões
	itensASeAdicionar = {}
	for coordenada, estado in grid4d.items():
		for coordenadaX in range(coordenada[0]-1,coordenada[0]+2):
			for coordenadaY in range(coordenada[1]-1,coordenada[1]+2):
				for coordenadaZ in range(coordenada[2]-1,coordenada[2]+2):
					for coordenadaW in range(coordenada[3]-1,coordenada[3]+2):
						coordenadaASeVerificar = (coordenadaX,coordenadaY,coordenadaZ,coordenadaW)
						if coordenadaASeVerificar not in grid4d and estado: 
							itensASeAdicionar[coordenadaASeVerificar] = False
	grid4d.update(itensASeAdicionar)

for numeroCiclo in range(6): 
	expandirGridEmTornoDosAtivos4d() 
	gridAposIteracao = {} 
	for coordenada, estado in grid4d.items():
		numeroDeCubosAtivosEmVolta = 0
		for coordenadaX in range(coordenada[0]-1,coordenada[0]+2):
			for coordenadaY in range(coordenada[1]-1,coordenada[1]+2):
				for coordenadaZ in range(coordenada[2]-1,coordenada[2]+2):
					for coordenadaW in range(coordenada[3]-1,coordenada[3]+2):
						coordenadaASeVerificar = (coordenadaX,coordenadaY,coordenadaZ,coordenadaW)
						if coordenadaASeVerificar in grid4d and coordenadaASeVerificar!=coordenada:
							numeroDeCubosAtivosEmVolta += grid4d[coordenadaASeVerificar]
		if estado == True:
			if numeroDeCubosAtivosEmVolta != 2 and numeroDeCubosAtivosEmVolta != 3:
				gridAposIteracao[coordenada] = False
		else:
			if numeroDeCubosAtivosEmVolta == 3:
				gridAposIteracao[coordenada] = True
	grid4d.update(gridAposIteracao)
numeroDeCubosAtivos = sum(grid4d.values())
print('[4D] Número de cubos ativos após 6 ciclos:', numeroDeCubosAtivos)
