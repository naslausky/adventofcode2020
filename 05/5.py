#Desafio do dia 05/12/2020
#a) Receber uma lista de números binários e descobrir qual é o maior (onde F ou L representam 0, e B ou R representam 1)
#b) Perceber qual número que está faltando na lista de números.

def SubstituirPorNumeroBinario(numero):
	numero = numero.replace("R","1")
	numero = numero.replace("L","0")
	numero = numero.replace("B","1")
	numero = numero.replace("F","0")
	return numero

with open("input.txt") as file:
	linhas = file.read().splitlines()
linhasEmBinario = [SubstituirPorNumeroBinario(x) for x in linhas]
numerosDosPasses = [int(x,2) for x in linhasEmBinario]
maiorNumero = max (numerosDosPasses)
print ("Maior número de embarque:", maiorNumero)

#Parte dois:
menorNumero = min (numerosDosPasses)
for id in range(menorNumero,maiorNumero):
	if id not in numerosDosPasses:
		print("Número que falta no meio da lista:", id)
