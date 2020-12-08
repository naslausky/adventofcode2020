#Desafio do dia 07/12/2020

#a) Receber uma lista de itens, e cada item tem uma lista de sub-itens também presentes na lista externa.
#   Calcular quantos itens podem conter um sub-item específico.
#b) Calcular quantos sub-itens esse item específico contém.

with open("input.txt") as file:
	linhas = file.read().splitlines()

dicionarioRequisitos = {} #Dicionário que relaciona as bolsas aos requisitos da forma: {bagAzul: {bagVermelha:4}...}

for linha in linhas:
	bagSuperior = linha.split(" contain ")[0]
	requisitos = linha.split(" contain ")[1]
	requisitos = requisitos.replace(".","")
	listaRequisitos = requisitos.split(", ")
	chave = bagSuperior.replace("bags","bag")
	if requisitos == "no other bags":
		valor = {}
	else:
		valor = {(" ".join(req.split()[1:]).replace("bags","bag")) : int(req.split()[0]) for req in listaRequisitos}
	dicionarioRequisitos[chave] = valor

bolsasVerificadas = set()
bolsasAVerificar = {"shiny gold bag"}

while len(bolsasAVerificar - bolsasVerificadas)!=0:
	for bolsa in (bolsasAVerificar - bolsasVerificadas):
		bolsasQueContemABolsa = [b for (b, requisitos) in dicionarioRequisitos.items() if bolsa in requisitos]
		bolsasAVerificar.update(bolsasQueContemABolsa)
		bolsasVerificadas.add(bolsa)

bolsasVerificadas.remove("shiny gold bag")
print("A bolsa dourada pode estar contida dentro de", len(bolsasVerificadas), "bolsas diferentes." )

#Parte 2
def numeroDeBolsasDentroDeOutra(bolsa):
	return sum([numero*numeroDeBolsasDentroDeOutra(b) for (b,numero) in dicionarioRequisitos[bolsa].items()])+1

numeroTotalDeBolsasNecessarias = numeroDeBolsasDentroDeOutra("shiny gold bag")
numeroTotalDeBolsasNecessarias -= 1 #Excluir a bolsa dourada mais externa
print("Sua bolsa precisa de", numeroTotalDeBolsasNecessarias, "outras bolsas dentro dela.")
