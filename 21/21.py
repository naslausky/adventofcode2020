#Desafio do dia 21/12/2020
#a)Receber uma lista de produtos. Cada produto contém uma lista de ingredientes e uma lista de alérgenos.
#  Cada alérgeno só está presente em um ingrediente. Verificar e contar quantos ingredientes não contém nenhum alérgeno.
#b)Listar os ingredientes que contém alérgenos, baseado na ordem alfabética dos alérgenos.

with open('input.txt') as file:
	linhas = file.read().splitlines()
dicionarioPossibilidadeAlergenos = {} #Dicionário que relaciona cada alérgeno a seus possíveis ingredientes.
for linha in linhas:
	ingredientes,alergenos = linha.split(' (')
	ingredientes = set(ingredientes.split())
	alergenos = alergenos[9:-1].replace(',','').split()
	for alergeno in alergenos: #Os ingredientes possíveis são a interseção dentre os ingredientes de cada produto.
		if alergeno in dicionarioPossibilidadeAlergenos:
			dicionarioPossibilidadeAlergenos[alergeno] = dicionarioPossibilidadeAlergenos[alergeno].intersection(ingredientes)
		else:
			dicionarioPossibilidadeAlergenos[alergeno] = ingredientes

setIngredientesCandidatos = set() #Ingredientes que podem conter um alérgeno.
for ingredientes in dicionarioPossibilidadeAlergenos.values(): 
	setIngredientesCandidatos.update(ingredientes)
numeroIngredientesSemAlergenos = 0
for linha in linhas: #Contar quantos ingredientes não contém nenhum alérgeno.
	ingredientes,alergenos = linha.split(" (")
	ingredientes = ingredientes.split()
	for ingrediente in ingredientes:
		if ingrediente not in setIngredientesCandidatos:
			numeroIngredientesSemAlergenos += 1
print("O número de ingredientes que com certeza não contém alérgenos é:", numeroIngredientesSemAlergenos)
#Parte 2:
gabaritoIngredientes = {}#Dicionário que relaciona cada ingrediente a seu alérgeno.
while (len(gabaritoIngredientes)!=len(dicionarioPossibilidadeAlergenos)):
	for alergeno,ingredientes in dicionarioPossibilidadeAlergenos.items():
		if len(ingredientes) == 1:
			ingrediente = next(iter(ingredientes))
			gabaritoIngredientes[ingrediente] = alergeno
	setGabarito = set(gabaritoIngredientes.keys())
	for alergeno in dicionarioPossibilidadeAlergenos:
		ingredientes = dicionarioPossibilidadeAlergenos[alergeno]
		dicionarioPossibilidadeAlergenos[alergeno] = ingredientes - setGabarito #Remove os ingredientes já descobertos.
listaAlergenos = list(gabaritoIngredientes.values())
listaAlergenos.sort() #Ordena alfabeticamente
listaIngredientes = []
for alergenoOrdenado in listaAlergenos:
	for ingrediente,alergeno in gabaritoIngredientes.items():
		if alergenoOrdenado == alergeno:
			listaIngredientes.append(ingrediente)
print("Lista de ingredientes perigosos:", ','.join(listaIngredientes))

