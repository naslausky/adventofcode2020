#Desafio do dia 14/12/2020
#a)Receber uma lista de posições na memória e valores a serem salvos. Salvar eles aplicando uma máscara a cada valor
#b)Aplicar a mascara agora em cada posição, onde uma máscara pode gerar múltiplas posições possíveis.

with open('input.txt') as file:
	linhas = file.read().splitlines()

mascaraAtual = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' #Máscara neutra caso a primeira linha não seja uma.
dicionarioPosicoesMemoria = {} #Dicionário que relaciona as posições de memória com seu conteúdo.
for instrucao in linhas:
	if 'mem' in instrucao:
		posicao, valor = instrucao.split(' = ')
		valor = int(valor)
		posicao = int(posicao[4:-1]) #Remove os primeiros caracteres "mem[" e o último "]"
		valorEmBinario = bin(valor)[2:].zfill(36) #Adiciona padding de zeros para encaixar na máscara
		listaDosBitsAposMascara = []
		for indice, bitMascara in enumerate(mascaraAtual):
			if bitMascara == 'X':
				listaDosBitsAposMascara.append(valorEmBinario[indice])
			else:
				listaDosBitsAposMascara.append(bitMascara)
		stringBitsAposMascara = ''.join(listaDosBitsAposMascara)
		valorAposMascara = int(stringBitsAposMascara,2) #Desnecessário. Apenas para comparar com os exemplos.
		dicionarioPosicoesMemoria[posicao] = valorAposMascara
	else:
		mascaraAtual = instrucao.split(" = ")[1]
somaDeTodosOsValoresPresentesnaMemoria = sum (dicionarioPosicoesMemoria.values())
print("A soma de todos os valores presentes em memória é:", somaDeTodosOsValoresPresentesnaMemoria)

#Parte 2:
mascaraAtual = '000000000000000000000000000000000000'#Neste caso, a máscara neutra é outra.
dicionarioPosicoesMemoria = {}
for instrucao in linhas:
	if 'mem' in instrucao:
		posicao,valor = instrucao.split(' = ')
		valor = int(valor)
		posicao = int(posicao[4:-1])
		posicaoEmBinario = bin(posicao)[2:].zfill(36)
		listaDosBitsAposMascara = [] #Lista dos caracteres da posição após aplicação da máscara.
		for indice, bitMascara in enumerate(mascaraAtual):
			if bitMascara == '1' or bitMascara == 'X':
				listaDosBitsAposMascara.append(bitMascara)
			else:
				listaDosBitsAposMascara.append(posicaoEmBinario[indice])
		stringBitsAposMascara = ''.join(listaDosBitsAposMascara) #!Desncessário talvez.
		listaPosicoesNaMemoria = [[]] #Lista de listas onde cada item representa uma posição de memória para salvar o valor.
		for indice, bitPosicao in enumerate(stringBitsAposMascara):
			if bitPosicao == 'X': #!Cada posição de lista vira duas, appendando 1 e 0. Deve dar pra fazer com compreensão.
				copiaLista = listaPosicoesNaMemoria[:]
				for posicaoPossivel in listaPosicoesNaMemoria:
					posicaoPossivelCom0 = posicaoPossivel+['0']
					posicaoPossivelCom1 = posicaoPossivel+['1']
					copiaLista.remove(posicaoPossivel)
					copiaLista.append(posicaoPossivelCom0)
					copiaLista.append(posicaoPossivelCom1)
				listaPosicoesNaMemoria = copiaLista
			else:
				for posicaoPossivel in listaPosicoesNaMemoria: #Não bifurca
					posicaoPossivel.append(stringBitsAposMascara[indice])
		for posicaoASeSalvarOValor in listaPosicoesNaMemoria:
			stringBinariaPosicao = ''.join(posicaoASeSalvarOValor)
			posicao = int(stringBinariaPosicao,2)
			dicionarioPosicoesMemoria[posicao] = valor
	else:
		mascaraAtual = instrucao.split(' = ')[1]
somaDeTodosOsValoresPresentesnaMemoria = sum (dicionarioPosicoesMemoria.values())
print("A soma de todos os valores presentes em memória é:", somaDeTodosOsValoresPresentesnaMemoria)
