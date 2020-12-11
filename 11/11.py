#Desafio do dia 11/12/2020
#a)Receber uma matriz de caracteres, e aplicar regras de transição sucessivamente até a matriz estabilizar.
#  Ao final, contabilizar o número de caractéres "#"
#b)Idem porém com um outro conjunto de regras.

with open("input.txt") as file:
	linhas = file.read().splitlines()
	#Adiciona uma camada de "chão" em torno de todo o mapa.
	for indiceLinha in range(0,len(linhas)):
		linhas[indiceLinha] = "."+linhas[indiceLinha]+"." 
	tamanhoDaLinha = len(linhas[0])
	linhas.insert(0,"."*tamanhoDaLinha)
	linhas.append("."*tamanhoDaLinha)
	linhasOriginais = linhas[:] #Guarda o estado original para poder resetar ao fazer a parte2

def executarRegras(linhas, Parte2 = False):
	#Função que executa uma iteração das regras de transição (Tanto da parte 1 quanto da parte 2)
	#Retorna as linhas após a iteração, e se houve modificação ou não.
	foiModificadoAlgumLugar = False
	linhasAposModificacao = linhas[:]
	for indiceLinha in range(1,len(linhas)-1):
		for indiceColuna in range(1,tamanhoDaLinha-1):
			espaco = linhas[indiceLinha][indiceColuna]
			numeroDeAssentosOcupados = (	numeroDeAssentosOcupadosAoRedor(indiceLinha,indiceColuna,linhas) 
							if not Parte2 else 
							numeroAssentosOcupadosNosAngulos(indiceLinha,indiceColuna,linhas))
			if espaco == "L":
				if numeroDeAssentosOcupados == 0:
					linhasAposModificacao = inverterEstadoDoLugar(indiceLinha, indiceColuna, linhasAposModificacao)
					foiModificadoAlgumLugar = True
			elif espaco == "#":
				if numeroDeAssentosOcupados >=(4 if not Parte2 else 5):
					linhasAposModificacao = inverterEstadoDoLugar(indiceLinha, indiceColuna, linhasAposModificacao)
					foiModificadoAlgumLugar = True
	linhas = linhasAposModificacao[:]
	return foiModificadoAlgumLugar, linhas


def numeroDeAssentosOcupadosAoRedor(indiceLinha, indiceColuna, linhas):
	#Função que retorna quantos assentos ocupados estão presentes ao redor de um indice
	numeroResultante = sum([x[indiceColuna-1:indiceColuna+2].count("#") for x in linhas[indiceLinha-1:indiceLinha+2]])
	if (linhas[indiceLinha][indiceColuna]) == "#":
		numeroResultante-=1 #Como eu contei dentro de um bloco 3x3, é preciso desconsiderar o elemento central.
	return numeroResultante

def numeroAssentosOcupadosNosAngulos(indiceLinha, indiceColuna, linhas):
	#Função que retorna quantos assentos ocupados podem ser vistos quando olha-se para cada direção.
	angulosParaVerificarAssentos = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
	numeroDeAssentosOcupadosVistos = 0
	for angulo in angulosParaVerificarAssentos:
		indiceVerticalDaBusca, indiceHorizontalDaBusca = (indiceLinha, indiceColuna)
		achouAssentoNoAngulo = False
		while ((indiceVerticalDaBusca in range(1,len(linhas)-1))
			and (indiceHorizontalDaBusca in range(1,tamanhoDaLinha-1))
			and not achouAssentoNoAngulo):
			indiceVerticalDaBusca+=angulo[0]
			indiceHorizontalDaBusca+=angulo[1]
			espacoAtual = linhas[indiceVerticalDaBusca][indiceHorizontalDaBusca]
			if ((espacoAtual == "L") or (espacoAtual == "#")):
				achouAssentoNoAngulo=True
				if espacoAtual=="#":
					numeroDeAssentosOcupadosVistos+=1
	return numeroDeAssentosOcupadosVistos

def contarLugaresOcupados(linhas):
	#Conta quantos lugares estão ocupados em todas as linhas
	return sum(linha.count("#") for linha in linhas)


def inverterEstadoDoLugar(indiceLinha, indiceColuna, linhasAposModificacao):
	#Função que inverte o estado do lugar indicado (entre livre e ocupado)
	if linhas[indiceLinha][indiceColuna] == "L":
		novoEstado = "#"
	else:
		novoEstado = "L"
	linhaAtual = linhasAposModificacao[indiceLinha]
	listaDaLinhaAtual = list(linhaAtual)
	listaDaLinhaAtual[indiceColuna]=novoEstado
	linhasAposModificacao[indiceLinha] = "".join(listaDaLinhaAtual)
	return linhasAposModificacao


modificou=True
while(modificou):
	modificou, linhas = executarRegras(linhas)
print("Número de lugares ocupados após primeiro conjunto de regras:", contarLugaresOcupados(linhas))


#Parte 2:

linhas = linhasOriginais[:] #Pega a disposição original novamente.
modificou = True
while (modificou):
	modificou, linhas = executarRegras(linhas, True)
print("Número de lugares ocupados após segundo conjunto de regras:", contarLugaresOcupados(linhas))
