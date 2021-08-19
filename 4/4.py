#Desafio do dia 04/12/2020
#a) Receber um texto com uma lista de campos e verificar para cada caso se tem algum campo faltando.
# Os casos são separados por linhas em branco.
#b) Dentre os casos válidos, verificar cada campo.

def converterPassaporteParaDicionario(passaporteStrings):
	#Função que converte um dicionário do tipo ['a:b',"b:c"...] para {"a":"b","c":d"...}
	passaporteCampos = {}
	for campo in passaporteStrings:
		chave , valor = campo.split(":")
		passaporteCampos[chave] = valor
	return passaporteCampos

passaportes = [] #lista de passaortes
passaporteAtual = [] #Um passaporte, que é uma lista de campos do tipo ['a:b','b:c'...]
with open ("input.txt") as file:
	for linha in file:
		if linha == "\n":
			#Chegou ao fim de um passaporte. Salvar na lista e começar um novo.
			passaportes.append(converterPassaporteParaDicionario(passaporteAtual))
			passaporteAtual=[]
		else:
			passaporteAtual.extend(linha.split())

#Adiciona o último passaporte que faltou (dado que o arquivo acaba acabando):
passaportes.append(converterPassaporteParaDicionario(passaporteAtual))

camposObrigatorios = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

#cid é opcional:
passaportesComTodosOsCampos = []
for passaporte in passaportes:
	contemTodosOsCampos = True
	for campo in camposObrigatorios:
		if campo not in passaporte:
			contemTodosOsCampos = False
	if contemTodosOsCampos:
		passaportesComTodosOsCampos.append(passaporte)
print("Quantidade de passaportes válidos: ", len(passaportesComTodosOsCampos))

#Segunda parte:
coresDeOlhoPossiveis = ["amb","blu","brn","gry","grn","hzl","oth"]
passaportesValidos = []
for passaporte in passaportesComTodosOsCampos:
	todosOsCamposValidos = True
	for chave, valor in passaporte.items():
		if (chave == "byr"):
			if(int(valor)<1920 or int(valor)>2002):
				todosOsCamposValidos = False
		elif chave == "iyr":
			if(int(valor)<2010 or int(valor)>2020):
				todosOsCamposValidos = False
		elif chave == "eyr":
			if(int(valor)<2020 or int(valor)>2030):
				todosOsCamposValidos = False
		elif chave == "hgt":
			if (valor[-2:] == "in"):
				if(int(valor[:-2])<59 or int(valor[:-2])>76):
					todosOsCamposValidos = False
			elif (valor[-2:]== "cm"):
				if(int(valor[:-2])<150 or int(valor[:-2])>193):
					todosOsCamposValidos = False
			else:
				todosOsCamposValidos = False
		elif chave == "hcl":
			if valor[0]!="#" or len(valor) !=7:
				todosOsCamposValidos = False
			try:
				int(valor[-6:],16)
			except:
				todosOsCamposValidos = False
		elif chave == "ecl":
			if valor not in coresDeOlhoPossiveis:
				todosOsCamposValidos = False
		elif chave == "pid":
			if len(valor)!=9:
				todosOsCamposValidos = False
			try:
				int(valor)
			except:
				todosOsCamposValidos = False
	if todosOsCamposValidos:
		passaportesValidos.append(passaporte)

print("Número de passaportes válidos: ", len(passaportesValidos))
