#Desafio do dia 18/12/2020
#a)Receber uma lista de expressões que envolvem soma e multiplicação, e resolver ignorando a precedência de operadores.
#b)Com a mesma lista, resolver utilizando a precedência de operadores inversa.

def avaliarExpressao(expressao):
	operadoresPossiveis = '+*'
	ultimoOperadorEncontrado = '+'
	indiceParaIgnorar = -1 #Caso seja encontrado uma abertura de parênteses, este será o índice do seu par.
	numeroAteAgora = [] #Buffer que contém os caracteres do próximo número
	resultado = 0
	for indice, caracter in enumerate(expressao):
		if indice<=indiceParaIgnorar:
			continue
		if caracter in operadoresPossiveis:
			stringNumeroDaVez = ''.join(numeroAteAgora).strip()
			if not stringNumeroDaVez: #Acabou de finalizar um parênteses
				ultimoOperadorEncontrado = caracter #Talvez não precisasse caso a recursão seguisse o mesmo padrão
				continue
			numeroDaVez = int(stringNumeroDaVez)
			numeroAteAgora = []
			if ultimoOperadorEncontrado == '+':
				resultado += numeroDaVez
			else:
				resultado *= numeroDaVez
			ultimoOperadorEncontrado = caracter
		elif caracter == '(':
			numeroParentesesAbertos = 0
			for indiceSegundoCaracter,segundoCaracter in enumerate(expressao[indice: len(expressao)]): #Encontrar o parênteses que fecha este.
				if segundoCaracter == ')':
					numeroParentesesAbertos -= 1
				elif segundoCaracter == '(':
					numeroParentesesAbertos += 1
				if numeroParentesesAbertos == 0:
					indiceParaIgnorar = indiceSegundoCaracter+indice
					subExpressao = expressao[indice+1:indiceParaIgnorar]
					if ultimoOperadorEncontrado == '+':
						resultado += avaliarExpressao(subExpressao) 
					else:
						resultado *= avaliarExpressao(subExpressao)
					break
		else:
	 		numeroAteAgora.append(caracter)
	stringNumeroDaVez = ''.join(numeroAteAgora).strip()
	if stringNumeroDaVez:
		numeroDaVez = int(stringNumeroDaVez)
		if ultimoOperadorEncontrado == '+':
			resultado += numeroDaVez
		else:
			resultado *= numeroDaVez
	return resultado
def avaliarExpressaoComPrecedenciaInvertida(expressao):	# Função que separa a expressão em elementos (fatores ou operadores). Calcula as somas primeiro.
	indiceParaIgnorar = -1 				#A ideia inicial era adicionar vários parênteses e re-utilizar a primeira função, mas desisti.
	operadoresPossiveis = '+*'			#Acabou que ficou uma função bem parecida com a primeira, porém levando em consideração a ordem.
	numeroAteAgora = []				#Isto é, poderia ser reaproveitado o processamento em comum.
	listaDaExpressao = [] #Lista da seguinte forma ['123','+','456,'*',...]
	for indice, caracter in enumerate(expressao):
		if indice<=indiceParaIgnorar:
			continue
		if caracter in operadoresPossiveis:
			stringNumeroDaVez = ''.join(numeroAteAgora).strip()
			if stringNumeroDaVez:
				listaDaExpressao.append(stringNumeroDaVez)
			listaDaExpressao.append(caracter)
			numeroAteAgora = []
		elif caracter == '(':
			numeroParentesesAbertos = 0
			for indiceSegundoCaracter, segundoCaracter in enumerate(expressao[indice:len(expressao)]):
				if segundoCaracter == ')':
					numeroParentesesAbertos -=1
				elif segundoCaracter == '(':
					numeroParentesesAbertos +=1
				if numeroParentesesAbertos == 0:
					indiceParaIgnorar = indiceSegundoCaracter+indice
					subExpressao = expressao[indice+1:indiceParaIgnorar]
					listaDaExpressao.append(avaliarExpressaoComPrecedenciaInvertida(subExpressao))
					break
		else:
			numeroAteAgora.append(caracter)
	stringNumeroDaVez = ''.join(numeroAteAgora).strip()
	listaDaExpressao.append(stringNumeroDaVez)
	expressaoFinal = ''.join(listaDaExpressao)
	expressaoFinal = expressaoFinal.split('*')
	resultadoMultiplicacao = 1
	for fator in expressaoFinal:
		resultadoMultiplicacao *= avaliarExpressao(fator) #Só existirão fatores simples do tipo (a+b).
	return str(resultadoMultiplicacao)

with open('input.txt') as file:
	expressoes = file.read().splitlines()
	somaDeTodasAsExpressoes = sum([avaliarExpressao(expressao) for expressao in expressoes])
	print("A soma do resultado de todas as expressões desconsiderando precedência é:", somaDeTodasAsExpressoes)
	somaDeTodasAsExpressoesComPrecedenciaInvertida = sum([int(avaliarExpressaoComPrecedenciaInvertida(expressao)) for expressao in expressoes])
	print("A soma do resultado de todas as expressões com a precedência invertida é:", somaDeTodasAsExpressoesComPrecedenciaInvertida)
