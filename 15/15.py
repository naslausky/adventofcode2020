#Desafio do dia 15/12/2020
#a)Receber uma lista de números e uma regra de formação dessa lista. Calcular o 2020º elemento dessa lista.
#b)Informar o 30000000º número dessa lista.

with open('input.txt') as file:
	linhas = file.read().splitlines()
	numeros = linhas[0].split(',')
	numeros = list(map(int,numeros))

def calcularEnesimoElementoDaSequencia(n, numerosIniciais):
	dicionarioDasUltimasVezesQueApareceu = {} #Dicionário que relaciona o número com o índice da última vez que ele apareceu.
	for indice, numero in enumerate(numerosIniciais): #inicializa o dicionário com os números iniciais.
		dicionarioDasUltimasVezesQueApareceu[numero] = indice+1
	numeroDitoMaisRecente = numerosIniciais[-1]

	for indiceNumero in range(len(numeros),n):
		if numeroDitoMaisRecente not in dicionarioDasUltimasVezesQueApareceu: #Primeira vez que o número é dito.
			dicionarioDasUltimasVezesQueApareceu[numeroDitoMaisRecente] = indiceNumero
			numeroDitoMaisRecente = 0
		else: #Número ja foi dito antes e salvo no dicionário o índice da última vez que apareceu.
			indiceDaPenultimaVezQueApareceu = dicionarioDasUltimasVezesQueApareceu[numeroDitoMaisRecente]
			numeroASeAdicionar = indiceNumero - indiceDaPenultimaVezQueApareceu
			dicionarioDasUltimasVezesQueApareceu[numeroDitoMaisRecente] = indiceNumero
			numeroDitoMaisRecente = numeroASeAdicionar
	return numeroDitoMaisRecente

print("O 2020º número da sequência é:", calcularEnesimoElementoDaSequencia(2020, numeros))
#Parte 2:
print("O 30000000º número da sequência é:", calcularEnesimoElementoDaSequencia(30000000, numeros))

#Tentativa inicial. Funciona porém muito dispendioso para números elevados.
#for indiceNumero in range(len(numeros), 2020):
#	numeroDitoMaisRecente = numeros[indiceNumero-1]
#	if numeros.count(numeroDitoMaisRecente) == 1: #Primeira vez que o número foi dito
#		numeros.append(0)
#	else: #Inverte a lista, verifica primeira ocorrência e compara os índices.
#		indiceDaPenultimaVezQueFoiDito = (indiceNumero-1) - list(reversed(numeros[:-1])).index(numeroDitoMaisRecente)
#		numeros.append(indiceNumero - indiceDaPenultimaVezQueFoiDito)
#print("O 2020º número da sequência é:", numeros[2019])
