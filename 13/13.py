#Desafio do dia 13/12/2020
#a) Receber uma lista de frequências de onibus e ver qual o primeiro ônibus que sai após um dado horário.
#b) Achar o primeiro valor que satisfaz uma equação modular dentre os onibus e os tempos sequenciais.

with open("input.txt") as file:
	linhas = file.read().splitlines()
	horarioDeChegadaAoTerminal = int(linhas[0])
	listaOnibus = linhas[1].split(",")
	listaOnibusEmServico = [id for id in listaOnibus if id!="x"]
	listaOnibusEmServico = list(map(int,listaOnibusEmServico))

idDoOnibusDeEsperaMinima = listaOnibusEmServico[0] #Inicializa com os valores do primeiro onibus
minimoTempoDeEspera = -horarioDeChegadaAoTerminal%idDoOnibusDeEsperaMinima

for idOnibus in listaOnibusEmServico: 
	tempoDeEsperaDoOnibusAtual = min(minimoTempoDeEspera, -horarioDeChegadaAoTerminal%idOnibus)
	if minimoTempoDeEspera != tempoDeEsperaDoOnibusAtual:
		minimoTempoDeEspera = tempoDeEsperaDoOnibusAtual
		idDoOnibusDeEsperaMinima = idOnibus

print(minimoTempoDeEspera, "minutos entre a sua chegada e a saida do onibus de id", idDoOnibusDeEsperaMinima)
print("Multiplicação dos valores:", minimoTempoDeEspera * idDoOnibusDeEsperaMinima)

#Parte 2:
def inversoModularDoNumero(numero, modulo): #Função que retorna o inverso de um número dado um módulo.
	for tentativaInverso in range(modulo):
		if (tentativaInverso*numero)%idOnibus==1:
			return tentativaInverso

#Dicionário que relaciona o idDoOnibus com o complementar de seu indice.
dicionarioRequisitos = {int(idOnibus): (int(idOnibus)-indice) for (indice, idOnibus) in enumerate(listaOnibus) if idOnibus !="x"}

multiplicacaoDeTodosOsModulos = 1 #Valor útil para o teorema chinês dos restos
for idOnibus,indice in dicionarioRequisitos.items():
	multiplicacaoDeTodosOsModulos *= idOnibus

#Resposta final: precisa ser congruente a cada indice do onibus, módulo a cada idOnibus
primeiroHorarioValido = 0
for idOnibus, indice in dicionarioRequisitos.items():
	Ma = int(multiplicacaoDeTodosOsModulos/idOnibus)
	inverso = inversoModularDoNumero(Ma,idOnibus)
	primeiroHorarioValido += inverso * Ma * indice
print("O primeiro horário válido que satisfaz a equação é:", primeiroHorarioValido%multiplicacaoDeTodosOsModulos)

#Parte 2 - Sem usar teorema chinês dos restos propriamente dito:
primeiroHorarioValido = 0
numeroAIncrementar = 1
for idOnibus in sorted(listaOnibusEmServico,reverse=True):#.sort(reverse=True):
	indice = dicionarioRequisitos[idOnibus]
#	if (primeiroHorarioValido%idOnibus == indice%idOnibus): #Caso em que em uma mesma incrementada acha dois casos
#			numeroAIncrementar *=idOnibus #Porém nos inputs que testei, nunca caiu nesse caso.
#			continue
	achou = False
	while not achou:
		primeiroHorarioValido +=numeroAIncrementar
		if (primeiroHorarioValido%idOnibus == indice%idOnibus):
			numeroAIncrementar *=idOnibus
			achou=True
print("O primeiro horário válido que satisfaz a equação é:", primeiroHorarioValido)
