#Desafio do dia 15/12/2020
#a)Receber uma lista de números e uma regra de formação dessa lista. Calcular o 2020º elemento dessa lista.
#b)Informar o 30000000º número dessa lista.

with open('input.txt') as file:
	linhas = file.read().splitlines()
	numeros = linhas[0].split(',')
	numeros = list(map(int,numeros))
	inputOriginal = numeros[:] #Para poder recomeçar na parte 2

dicionarioDasUltimasVezesQueApareceu = {} #Dicionário que relaciona o número com o índice da última vez que ele apareceu.
for indice, numero in enumerate(numeros): #inicializa o dicionário com os números iniciais.
	dicionarioDasUltimasVezesQueApareceu[numero] = indice+1
numeroDitoMaisRecente = numeros[-1]

for indiceNumero in range(len(numeros),30000000):
	if numeroDitoMaisRecente not in dicionarioDasUltimasVezesQueApareceu: #Primeira vez que o número é dito.
		dicionarioDasUltimasVezesQueApareceu[numeroDitoMaisRecente] = indiceNumero
		numeroDitoMaisRecente = 0
	else:
		indiceDaPenultimaVezQueApareceu = dicionarioDasUltimasVezesQueApareceu[numeroDitoMaisRecente]
		numeroASeAdicionar = indiceNumero - indiceDaPenultimaVezQueApareceu
		dicionarioDasUltimasVezesQueApareceu[numeroDitoMaisRecente] = indiceNumero
		numeroDitoMaisRecente = numeroASeAdicionar

print("O 30000000 número da sequência é:",numeroDitoMaisRecente)
#for indiceNumero in range(len(numeros), 2020):
#	numeroDitoMaisRecente = numeros[indiceNumero-1]
#	if numeros.count(numeroDitoMaisRecente) == 1: #Primeira vez que o número foi dito
#		numeros.append(0)
#	else: #Inverte a lista, verifica primeira ocorrência e compara os índices.
#		indiceDaPenultimaVezQueFoiDito = (indiceNumero-1) - list(reversed(numeros[:-1])).index(numeroDitoMaisRecente)
#		numeros.append(indiceNumero - indiceDaPenultimaVezQueFoiDito)
#print("O 2020º número da sequência é:", numeros[2019])
