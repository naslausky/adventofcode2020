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
#A estratégia aqui foi: 
#1) Perceber que as regras recursivas são: -(N múltiplas strings que satisfazem a regra 42 seguidas)
# e (M mensagens que adequam-se a regras 42 ao lado do mesmo número M de mensagens para as regras 31)
#2) Como a regra zero precisa das duas regras acima seguidas, logo, são (M+N) strings que satisfazem a 42, mais M que satisfazem a 31.
#3) Para cada mensagem, ir removendo regras 42 até onde der, depois remover as 31 e ver se a quantidade de remoções é plausível (M>N>0).

tamanhoRegra42 = [len(mensagem) for mensagem in dicionarioRegras[42]][0]  #Para adequar-se aos casos exemplo também.
tamanhoRegra31 = [len(mensagem) for mensagem in dicionarioRegras[31]][0]
numeroDeMensagensQueSatisfazemARegra0 = 0
for mensagem in linhasMensagens:
	palavraReduzida = mensagem
	remocoesDo42 = remocoesDo31 = 0 #Contabilizar o número.
	while palavraReduzida[:tamanhoRegra42] in dicionarioRegras[42]: #Remove exemplos de regra 42 do começo de cada mensagem.
			palavraReduzida = palavraReduzida[tamanhoRegra42:]
			remocoesDo42 += 1

	while palavraReduzida[-tamanhoRegra31:] in dicionarioRegras[31]: #Remove exemplos de regra 31 do final de cada mensagem.
			palavraReduzida = palavraReduzida[:-tamanhoRegra31]
			remocoesDo31 += 1

	if not palavraReduzida: #Não pode ter sobrado nada no final.
		if remocoesDo42 > 0 and remocoesDo31 > 0: #Precisa ter feito no mínimo 1 remoção de cada
			if remocoesDo42 > remocoesDo31: #Precisa ter removido mais do 42 pois está presente na regra 8 e na 11.
				numeroDeMensagensQueSatisfazemARegra0 += 1	
print("Número de mensagens que satisfazem a regra 0 após a substituição das regras:", numeroDeMensagensQueSatisfazemARegra0)
