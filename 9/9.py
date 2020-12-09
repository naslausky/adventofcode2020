#Desafio do dia 09/12/2020
#a)Receber uma lista de números em que cada item pode ser obtido como a soma de 2 itens dentre os 25 que o antecedem.
#  Verificar qual o primeiro item da lista que não segue essa regra.
#b)Verificar uma sequência de itens seguidos que somados são iguais a esse número. Obter a soma do maior e menor elementos dessa sequência.

with open("input.txt") as file:
	linhas = file.read().splitlines()
	linhas = list(map(int,linhas))

for indice in range(25,len(linhas)):
	numerosAnteriores = linhas[indice-25:indice]
	#Se nos últimos 25 números houver o mesmo item duas vezes, a possibilidade da soma deles não será cogitada.
	candidatosASoma = [(x,y) for x in numerosAnteriores for y in numerosAnteriores if x!=y and x+y==linhas[indice]]
	if not candidatosASoma:
		numeroAQuebrarARegra = linhas[indice]
		print("Primeiro número a quebrar a regra:", linhas[indice])
		break 

#Parte 2
for quantidadeDeElementosContiguos in range(2,len(linhas)+1):
	for indiceDoPrimeiroElemento in range(0,len(linhas)-quantidadeDeElementosContiguos+1):
		conjuntoAtual = linhas[indiceDoPrimeiroElemento : indiceDoPrimeiroElemento+quantidadeDeElementosContiguos]
		somaDoConjuntoAtual = sum(conjuntoAtual)
		if somaDoConjuntoAtual==numeroAQuebrarARegra:
			menorElemento = min(conjuntoAtual)
			maiorElemento = max(conjuntoAtual)
			print("Menor elemento:", menorElemento, "Maior elemento:",maiorElemento, "Soma:", maiorElemento+menorElemento)
