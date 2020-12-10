#Desafio do dia 10/12/2020
#a) Receber uma lista de números e após ordená-los verificar quais dentre eles possuem a diferença de 1 para o anterior. Multiplicar pelo numero de itens que possuem diferença de 3 para o anterior.
#b) Verificar quantas sub-listas existem em que cada uma delas números subsequentes não tenham uma diferença maior do que 3.
#Obs: Duas caracteristicas da entrada não foram ditas no enunciado, porém foram observadas no input. 
#Se alguma delas não fosse verdade, esse programa precisaria ser adaptado.
#São elas: (1) No input, não houve adaptadores com diferença de 2 entre si.
#(2) Não houve uma sequência com mais de 3 adaptadores com diferença de 1 entre si.

with open ("input.txt") as file:
	voltagens = file.read().splitlines()
	voltagens = list(map(int,voltagens))
	voltagens.append(0) #Voltagem da tomada na parede
	voltagens.sort()

voltagemAnterior = 0
diferencasDeVoltagens = []
for voltagem in voltagens:
	diferencasDeVoltagens.append(voltagem - voltagemAnterior)
	voltagemAnterior = voltagem

numeroDeDiferencasDe1Volt = diferencasDeVoltagens.count(1)
numeroDeDiferencasDe3Volts = diferencasDeVoltagens.count(3) + 1 #Precisa contar o último dispositivo conectado aos adaptadores.

print("Multiplicação dentre os adaptadores com diferença de 1 e 3 volts:", 
	numeroDeDiferencasDe1Volt*numeroDeDiferencasDe3Volts)

#Parte2
def sequenciasDeAdaptadoresRemoviveis(voltagens):
	#Alguns adaptadores são removiveis, outros não.
	#Eles são removíveis se a distancia para o elemento anterior e o seguinte é menor que 3.
	#Esta função retorna uma lista de listas desses números que são subsequentes no input. 
	todasAsSequencias=[]
	sequenciaAtual = []
	for indiceAdaptador in range (1,len(voltagens)-1):
		voltagemAnterior = voltagens[indiceAdaptador-1]
		voltagemAtual = voltagens[indiceAdaptador]
		voltagemSeguinte = voltagens[indiceAdaptador+1]
		if voltagemSeguinte-voltagemAnterior<=3:
			sequenciaAtual.append(voltagemAtual)
		else:
			if sequenciaAtual:
				todasAsSequencias.append(sequenciaAtual)
				sequenciaAtual=[]
	if sequenciaAtual: #Caso o último caso não tenha passado.
		todasAsSequencias.append(sequenciaAtual) 
	return todasAsSequencias

multiplicacaoDasPossibilidades = 1
for i in sequenciasDeAdaptadoresRemoviveis(voltagens):
	combinacoesPossiveisDessaSequencia = 1 #A própria sequência sem remover nenhum elemento
	combinacoesPossiveisDessaSequencia += len(i) #Removendo 1 adaptador podemos escolher dentre len(i)
	combinacoesPossiveisDessaSequencia += len(i) * (len(i)-1) /2 #Combinacao 3, 2 a 2
	multiplicacaoDasPossibilidades *= combinacoesPossiveisDessaSequencia #Por (2) citado acima, quaisquer dois adaptadores escolhidos nessa combinação são válidos.
print("Número de combinações possíveis de adaptadores:", int(multiplicacaoDasPossibilidades))
