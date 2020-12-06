#Desafio do dia 06/12/2020
#a) Em cada caso ver quantas letras diferentes apareceram, e somar todas essas ocorrências
#b) Em cada daso ver quantas letras apareceram em comum por todas as linhas, e somar essas ocorrências

conjuntoDePerguntasAtual = set()
listaDeGrupos = []

#Parte 2
conjuntoDePerguntasIntersecao = None
listaDeGruposIntersecao = []
with open ("input.txt") as file:
	for linha in file:
		if linha == "\n":
		#Chegou ao final de um grupo de passageiros
			listaDeGrupos.append(conjuntoDePerguntasAtual)
			conjuntoDePerguntasAtual = set()

			#Parte 2
			listaDeGruposIntersecao.append(conjuntoDePerguntasIntersecao)
			conjuntoDePerguntasIntersecao = None
		else:
			textoASeInserir = linha.replace("\n","")
			conjuntoDePerguntasAtual.update(textoASeInserir)
	
			#Parte 2 - Verifica a interseção entre os sets
			if conjuntoDePerguntasIntersecao == None:
				conjuntoDePerguntasIntersecao = set()
				conjuntoDePerguntasIntersecao.update(textoASeInserir)
			else:
				setDoPassageiroAtual = set()
				setDoPassageiroAtual.update(textoASeInserir)
				conjuntoDePerguntasIntersecao = conjuntoDePerguntasIntersecao.intersection(setDoPassageiroAtual)

#Adiciona o último caso que faltou (dado que o arquivo não termina com linha em branco):
listaDeGrupos.append(conjuntoDePerguntasAtual)
listaDeGruposIntersecao.append(conjuntoDePerguntasIntersecao)

numeroDeQuestoesRespondidas = 0
for grupo in listaDeGrupos:
	numeroDeQuestoesRespondidas += len(grupo)
#Parte 2
numeroDeQuestoesRespondidasPorTodosNoGrupo = 0
for grupo in listaDeGruposIntersecao:
	numeroDeQuestoesRespondidasPorTodosNoGrupo += len(grupo)

print ("Soma do número de questões respondidas em cada grupo: "+ str(numeroDeQuestoesRespondidas))
#Parte 2:
print("Soma do número de questões respondidas por todos em um mesmo grupo: "+ str(numeroDeQuestoesRespondidasPorTodosNoGrupo))
