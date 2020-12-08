#Desafio do dia 08/12/2020
#a)Receber uma lista de instruções simples (jump, acc e nop). 
#  Calcular o valor do registrador quando houver a primeira repetição de instrução.
#b)Alterar uma instrução para permitir o programa a encerrar devidamente. 
#  Neste caso, calcular o valor do registrador no término do programa.

with open("input.txt") as file:
	instrucoes = file.read().splitlines()

def seguirInstrucoes():
	acumulador = 0
	indiceDaInstrucao = 0
	instrucoesJaExecutadas = []
	while (indiceDaInstrucao not in instrucoesJaExecutadas) and not (indiceDaInstrucao>=len(instrucoes)):
		comando, valor = instrucoes[indiceDaInstrucao].split()
		valor = int(valor)
		instrucoesJaExecutadas.append(indiceDaInstrucao)
		if comando == "acc":
			acumulador += valor
			indiceDaInstrucao+=1
		elif comando == "jmp":
			indiceDaInstrucao+=valor
		else: #nop
			indiceDaInstrucao+=1
	encerrouNormalmente = (indiceDaInstrucao == len(instrucoes))
	return (encerrouNormalmente, acumulador)

def trocaInstrucao(instrucao):
	if "jmp" in instrucao:
		return instrucao.replace("jmp","nop")
	else:
		return instrucao.replace("nop","jmp")

concluiuComExito, valorAcumulador = seguirInstrucoes()
print("Valor do acumulador antes de uma operação repetida:", valorAcumulador)

#Parte 2
for indiceDaInstrucaoASerAlterada in range(0,len(instrucoes)):
	instrucoes[indiceDaInstrucaoASerAlterada] = trocaInstrucao(instrucoes[indiceDaInstrucaoASerAlterada])
	concluiuComExito, valorAcumulador = seguirInstrucoes()
	if concluiuComExito:
		print("Valor do acumulador antes do programa concluir com êxito:", valorAcumulador)
		print("Para isso foi trocada a instrução:", indiceDaInstrucaoASerAlterada)
		break
	#Troca de volta e segue o baile:
	instrucoes[indiceDaInstrucaoASerAlterada] = trocaInstrucao(instrucoes[indiceDaInstrucaoASerAlterada])
	
