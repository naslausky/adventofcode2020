#Desafio do dia 03/12/2020
#a) Receber uma matriz de caracteres e contar quantos X existem em uma diagonal específica
#b) Contar quantos X existem em várias diagonais e multiplicar esses números

def contarArvoresNaDescida(angulo):
	variacaoHorizontal = angulo[0]
	variacaoVertical = angulo[1]
	posicaoHorizontal = 0
	numeroDeArvores = 0
	for posicao in range(0,len(linhas),variacaoVertical):
		linha = linhas[posicao]
		tamanhoDaLinha = len(linha)
		if linha[posicaoHorizontal % tamanhoDaLinha]=="#":
			numeroDeArvores+=1
		posicaoHorizontal+=variacaoHorizontal
	return numeroDeArvores

with open("input.txt") as file:
	linhas = file.read().splitlines()

angulos = [(1,1),(3,1),(5,1),(7,1),(1,2)]

multiplicacaoDoNumeroDeArvores = 1
for angulo in angulos:
	print("Numero de arvores encontradas no angulo: " + str(angulo))
	numeroDeArvoresEncontradas = contarArvoresNaDescida(angulo)
	print(numeroDeArvoresEncontradas)
	multiplicacaoDoNumeroDeArvores*=numeroDeArvoresEncontradas

print("Multiplicação de todos os números encontrados: " + str(multiplicacaoDoNumeroDeArvores))
