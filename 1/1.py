# -*- coding: utf-8 -*-
#Desafio do dia 01/12/2020
#a)Receber uma lista de números, e verificar qual par tem soma 2020
#b)Verificar qual trio tem soma 2020

with open ("input.txt") as file:
	numeros = file.read().splitlines()
	numeros = list(map(int,numeros))
dicionarioModulos = {}
for numero in numeros:
	ultimoDigito = numero % 10
	if (ultimoDigito in dicionarioModulos):
		dicionarioModulos[ultimoDigito].append(numero)
	else:
		dicionarioModulos[ultimoDigito] = [numero]

for chave, valor in dicionarioModulos.items():
	if (10-chave) in dicionarioModulos:
		a = [(x,y) for x in dicionarioModulos[10-chave] for y in valor if x+y==2020]
		if a:
			parEncontrado = a[0]
			print(f"Encontrado os valores: {parEncontrado[0]} e {parEncontrado[1]}.")
			print(f"Multiplicação: {parEncontrado[0]*parEncontrado[1]}")
			break

print("Segunda parte:")

b = [(x,y,z) for x in numeros for y in numeros for z in numeros if (x+y+z)==2020]
if b:
	trioEncontrado = b[0]
	print(f"Encontrado os valores: {trioEncontrado[0]}, {trioEncontrado[1]} e {trioEncontrado[2]}.")
	print(f"Multiplicação: {trioEncontrado[0] * trioEncontrado[1] * trioEncontrado[2]}.")
