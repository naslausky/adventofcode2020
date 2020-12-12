#Desafio do dia 12/12/2020
#a)Receber uma série de instruções de movimentação. Calcular a norma 0 (Manhattan) ao final da sequência de instruções.
#b)Calcular a mesma norma porém com as instruções representando a variação em um vetor de direção. 
#  Apenas um dos comandos movimenta baseado nesse vetor.

from math import sin, cos,pi
with open("input.txt") as file:
	linhas = file.read().splitlines()

coordenadasDoBarco = [0,0] #[coordenadahorizontal, coordenadaVertical] 
#Caso o barco esteja nordeste ambas serão positivas.
direcaoDoBarco = 0 #Sentido cartesiano: ângulos positivos refletem o ato de girar no sentido anti-horário.

for instrucao in linhas:
	comando = instrucao[0]
	valor = int(instrucao[1:])
	if comando == "N":
		coordenadasDoBarco[1] += valor
	if comando == "S":
		coordenadasDoBarco[1] -= valor
	if comando == "E":
		coordenadasDoBarco[0] += valor
	if comando == "W":
		coordenadasDoBarco[0] -= valor
	if comando == "L":
		direcaoDoBarco += valor
	if comando == "R":
		direcaoDoBarco -= valor
	if comando == "F":
		coordenadasDoBarco[0] += cos(2*pi*(direcaoDoBarco/360.0)) * valor
		coordenadasDoBarco[1] += sin(2*pi*(direcaoDoBarco/360.0)) * valor
distanciaManhattan = abs(coordenadasDoBarco[0])+abs(coordenadasDoBarco[1]) #Norma 0
distanciaManhattan = int(round(distanciaManhattan)) #Arredondamento por conta do seno/cosseno tirados
print("Distância Manhattan da posição final do barco:", distanciaManhattan)

#Parte 2:
coordenadasDoBarco = [0,0]
coordenadasDoVetorDeDirecao = [10,1]

for instrucao in linhas:
	comando = instrucao[0]
	valor = int(instrucao[1:])
	if comando == "N":
		coordenadasDoVetorDeDirecao[1] += valor
	if comando == "S":
		coordenadasDoVetorDeDirecao[1] -= valor
	if comando == "E":
		coordenadasDoVetorDeDirecao[0] += valor
	if comando == "W":
		coordenadasDoVetorDeDirecao[0] -= valor
	if comando == "L":
		numeroDeVezesARotacionar = int(valor/90.0)
		for i in range(numeroDeVezesARotacionar):
			eixoX = coordenadasDoVetorDeDirecao[0]
			eixoY = coordenadasDoVetorDeDirecao[1]
			coordenadasDoVetorDeDirecao = [-eixoY,eixoX]
	if comando == "R":
		numeroDeVezesARotacionar = int(valor/90.0)
		for i in range(numeroDeVezesARotacionar):
			eixoX = coordenadasDoVetorDeDirecao[0]
			eixoY = coordenadasDoVetorDeDirecao[1]
			coordenadasDoVetorDeDirecao = [eixoY,-eixoX]
	if comando == "F":
		coordenadasDoBarco[0] += coordenadasDoVetorDeDirecao[0] * valor
		coordenadasDoBarco[1] += coordenadasDoVetorDeDirecao[1] * valor

print("Distância Manhattan da posição final do barco seguindo as novas regras:", abs(coordenadasDoBarco[0])+abs(coordenadasDoBarco[1]))
