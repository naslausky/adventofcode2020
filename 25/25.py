#Desafio do dia 25/12/2020
#a)Receber uma chave publica e obter a chave privada de cada elemento. Encriptar uma chave pública par-privada.
#b)
with open('input.txt') as file:
	linhas = file.read().splitlines()
	chavePublicaPorta = int(linhas[0])
	chavePublicaCartao = int(linhas[1])
def passoIteracao(numero,numeroInicial):#Função que itera uma vez seguindo os passos do handshake.
	modulo = 20201227
	numero = numero * numeroInicial
	return numero % modulo
def obterNumeroDeIteracoes(chavePublica): #Função que faz os passos e conta o número de iterações.
	valor = 1
	numeroDeIteracoes = 0
	while valor != chavePublica:
		valor = passoIteracao(valor, 7)
		numeroDeIteracoes+=1
	return numeroDeIteracoes
def obterChaveEncriptacao(numeroInicial,numeroDeIteracoes):
	modulo = 20201227
	valor = 1
	for i in range(numeroDeIteracoes):
		valor = passoIteracao(valor,numeroInicial)
	return valor
numeroDeIteracoesCartao = obterNumeroDeIteracoes(chavePublicaCartao)
#numeroDeIteracoesPorta = obterNumeroDeIteracoes(chavePublicaPorta)
chaveDeEncriptacao = obterChaveEncriptacao(chavePublicaPorta,numeroDeIteracoesCartao)
print("A chave de encriptação é:", chaveDeEncriptacao)
#Parte 2:
