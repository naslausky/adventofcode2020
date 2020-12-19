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
				#print("A regra",indice, "pode ser descoberta")
				possibilidades = texto.split(' | ')
				combinacoesDessaRegra = []
				#print("Possibilidades: ", possibilidades)
				for possibilidade in possibilidades:
					regrasDessaPossibilidade = possibilidade.split(' ')
					regrasDessaPossibilidade = list(map(int,regrasDessaPossibilidade))
					#print("Regras dessa possibilidade:", regrasDessaPossibilidade)
					combinacoesDessaPossibilidade = []
					for componente in regrasDessaPossibilidade:
						if combinacoesDessaPossibilidade:
							combinacoesDessaPossibilidade = [combinacao1 + combinacao2
											for combinacao1 in combinacoesDessaPossibilidade
											for combinacao2 in dicionarioRegras[componente]]
						else:
							combinacoesDessaPossibilidade = dicionarioRegras[componente]
						#print("Analisando componente:",componente)
						#print("Retorno das combinações: ", combinacoesDessaPossibilidade)
					combinacoesDessaRegra.extend(combinacoesDessaPossibilidade)
				#print("Adicionando", combinacoesDessaRegra, "ao indice", indice)
				#input()
				dicionarioRegras[indice] = set(combinacoesDessaRegra) #Provavelmente é melhor usar um set para evitar combinações repetidas.
	#for chave in dicionarioRegras:
		#dicionarioRegras[chave] = set(dicionarioRegras[chave])
	#print(dicionarioRegras)
	#input()
numeroDeMensagensQueSatisfazemARegra0 = sum([mensagem in dicionarioRegras[0] for mensagem in linhasMensagens])
print("Número de mensagens que satisfazem a regra 0:", numeroDeMensagensQueSatisfazemARegra0)
