with open('input.txt') as file:
	linhas = file.read().splitlines()
	linhasRegras = [] 
	linhasMensagens = []
	dicionarioRegras = {} #Dicionario que relaciona o indice da regra ao seu conjunto de possibilidades
	for linha in linhas:
		if ':' in linha: #É uma regra
			linhasRegras.append(linha)
		elif linha:
			linhasMensagens.append(linha)
def criarDicionarioRegrasBaseadoNasLinhas():
	for regra in linhasRegras:
		if '"' in regra: #Pega as regras que não dependem de outras primeiro.
			indice, texto = regra.split(':')
			dicionarioRegras[int(indice)] = [texto.strip()[1]]

	while(len(dicionarioRegras) != len(linhasRegras)): #Descobrir as possibilidades de todas as regras
		for regra in linhasRegras:
			indice, texto = regra.split(': ')
			indice = int(indice)
			if indice not in dicionarioRegras: #É uma regra que ainda não foi descoberta
				possibilidades = texto.split(' | ')
				permiteDescobrirTodasAsCombinacoes = True
				for possibilidade in possibilidades:
					regrasDessaPossibilidade = possibilidade.split(' ')
					regrasDessaPossibilidade = list(map(int,regrasDessaPossibilidade))
					for numeroDaRegra in regrasDessaPossibilidade:
						if numeroDaRegra not in dicionarioRegras:
							permiteDescobrirTodasAsCombinacoes = False
				if permiteDescobrirTodasAsCombinacoes: #Descobrir as possibilidades dela e adiciona ao dic.
					possibilidades = texto.split(' | ')
					combinacoesDessaRegra = []
					for possibilidade in possibilidades:
						regrasDessaPossibilidade = possibilidade.split(' ')
						regrasDessaPossibilidade = list(map(int,regrasDessaPossibilidade))
						combinacoesDessaPossibilidade = []
						for componente in regrasDessaPossibilidade:
							if combinacoesDessaPossibilidade:
								combinacoesDessaPossibilidade = [combinacao1 + combinacao2
												for combinacao1 in combinacoesDessaPossibilidade
												for combinacao2 in dicionarioRegras[componente]]
							else:
								combinacoesDessaPossibilidade = dicionarioRegras[componente]
						combinacoesDessaRegra.extend(combinacoesDessaPossibilidade)
					#print("Adicionando", combinacoesDessaRegra, "ao indice", indice)
					#input()
					dicionarioRegras[indice] = set(combinacoesDessaRegra) #Provavelmente é melhor usar um set para evitar combinações repetidas.
dicionarioRegras = {}
criarDicionarioRegrasBaseadoNasLinhas()
numeroDeMensagensQueSatisfazemARegra0 = sum([mensagem in dicionarioRegras[0] for mensagem in linhasMensagens])
print("Número de mensagens que satisfazem a regra 0:", numeroDeMensagensQueSatisfazemARegra0)

#Parte 2:
#Somente a regra 0 utiliza as regras 8 e 11. Essas em suas versões modificadas só possibilitam mensagens maiores.
#Verificar quais mensagens são maiores do que o tamanho usual:
tamanhoDasMensagensPossiveis = [len(mensagem) for mensagem in dicionarioRegras[0]]
tamanhoMensagem = tamanhoDasMensagensPossiveis[0]
mensagensMaiores = [mensagem for mensagem in linhasMensagens if len(mensagem)>tamanhoMensagem]
mensagensMaioresComTamanhoMultiploDe8 = [mensagem for mensagem in mensagensMaiores if len(mensagem)%8==0]
tamanhoMaiorMensagem = max([len(mensagem) for mensagem in mensagensMaiores])
tamanhoRegra42 = [len(mensagem) for mensagem in dicionarioRegras[42]][0]
tamanhoRegra31 = [len(mensagem) for mensagem in dicionarioRegras[31]][0]
tamanho31Mais42 = tamanhoRegra42 + tamanhoRegra31
novasMensagensPossiveis = set()
for mensagemOriginal in dicionarioRegras[42]:
	for i in range(1,int((tamanhoMaiorMensagem/tamanhoRegra42)+1)):
		novasMensagensPossiveis.add(mensagemOriginal*i)
#	for mensagemOriginal31 in dicionarioRegras[31]:
#		for i in range (1,tamanhoMaiorMensagem//tamanho31Mais42):
#			novasMensagensPossiveis.add((mensagemOriginal*i) + (mensagemOriginal31*i))

#Tentativa 2:
mensagensValidas = set()
for mensagem in mensagensMaiores:
	for mensagemPossivel42 in dicionarioRegras[42]:
		if mensagemPossivel42 in mensagem: #
			for i in range(1,int(tamanhoMaiorMensagem/tamanhoRegra42)+1):
				#print(mensagemPossivel42*i)
				if mensagem == (mensagemPossivel42*i):#Mensagem Valida
					#Por algum motivo a primeira regra não encaixa em nenhuma????
					mensagensValidas.add(mensagem)
	for mensagemPossivel11 in dicionarioRegras[11]:
		if mensagemPossivel11 in mensagem:
			pass
			#Essa Mensagem	tem o miolo uma mensagem do 11
#print(mensagensMaiores)
#input()
numeroDeMensagensQueSatisfazemARegra0Recursiva = sum([mensagem in novasMensagensPossiveis for mensagem in mensagensMaiores])

print("OutroNumero", numeroDeMensagensQueSatisfazemARegra0Recursiva)
