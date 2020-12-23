#Desafio do dia 23/12/2020
#a)Receber uma lista circular de números. Realizar um conjunto de instruções 100 vezes para retornar o estado final.
#b)Idem, porém com uma lista com 1 milhão de elementos e as instruções 10 milhões de vezes.
with open('input.txt') as file:
	linha = file.read().splitlines()[0]
	copos = []
	for numero in linha:
		copos.append(int(numero))
	coposParte2 = list(range(1,1000001)) #Copos da parte 2. Igual ao da parte 1 porém completo até 1 milhão.
	for indice,numeroCopo in enumerate(copos):
		coposParte2[indice] = numeroCopo
indiceCopoAtual = 0
for movimento in range(100):
	copoAtual = copos[indiceCopoAtual]
	coposDuplicados = copos+copos #Modo fácil de simular o círculo. Impraticável para listas grandes.
	coposRemovidos = coposDuplicados[indiceCopoAtual+1:indiceCopoAtual+4]
	copos = [copo for copo in copos if copo not in coposRemovidos]
	copoDestino = copoAtual -1
	while copoDestino not in copos:
		copoDestino -= 1
		if copoDestino<min(copos):
			copoDestino = max(copos)
	indiceCopoDestino = copos.index(copoDestino)
	copos = copos[:indiceCopoDestino + 1] + coposRemovidos + copos[indiceCopoDestino+1:]
	indiceCopoAtual = copos.index(copoAtual) + 1
	indiceCopoAtual = indiceCopoAtual % len(copos)
indiceCopoDeNumero1 = copos.index(1)
coposOrdenados = copos[indiceCopoDeNumero1+1:] + copos[:indiceCopoDeNumero1]
print("Os copos após o de número 1 são:", ''.join(str(copo) for copo in coposOrdenados))
#Parte 2
class Copo:
	def __init__ (self, numeroCopo):
		self.numero = numeroCopo
		self.proximo = None
copos = coposParte2
dicionarioCopos = {numero:Copo(numero) for numero in copos} #Dicionário da forma: {2:Copo2,...}
for indice, numeroCopo in enumerate(copos):#Provavelmente dá pra fazer isso numa varrida só.
	dicionarioCopos[numeroCopo].proximo = dicionarioCopos[copos[(indice+1)%len(copos)]]
copoAtual = dicionarioCopos[copos[0]] #Começa com o primeiro da lista
for movimento in range(10000000):
	primeiroCopoRemovido = copoAtual.proximo
	ultimoCopoRemovido = primeiroCopoRemovido.proximo.proximo #Remove 3 copos.
	copoAtual.proximo = ultimoCopoRemovido.proximo #Fecha o buraco que ficou.
	numerosDosCoposRemovidos = (primeiroCopoRemovido.numero,primeiroCopoRemovido.proximo.numero, ultimoCopoRemovido.numero)
	numeroCopoDestino = copoAtual.numero -1
	if numeroCopoDestino == 0:
		numeroCopoDestino = 1000000
	while (numeroCopoDestino in numerosDosCoposRemovidos):
		numeroCopoDestino -=1
		if numeroCopoDestino == 0:
			numeroCopoDestino = 1000000
	copoDestino = dicionarioCopos[numeroCopoDestino]
	copoAposODestino = copoDestino.proximo #Os copos removidos devem ser inseridos entre esses dois.
	copoDestino.proximo = primeiroCopoRemovido
	ultimoCopoRemovido.proximo = copoAposODestino
	copoAtual = copoAtual.proximo
copo1 = dicionarioCopos[1].proximo
copo2 = copo1.proximo
print("A multiplicação dos dois copos após o de número 1 é:", (copo1.numero * copo2.numero))
