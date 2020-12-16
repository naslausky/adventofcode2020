#Desafio do dia 16/12/2020
#a)Receber uma lista de regras e uma lista de conjuntos de números. Verificar quais conjuntos possuem números que são impossíveis de se adequar as regras.
#b)Deduzir quais campos representam quais regras.

with open('input.txt') as file:
	linhas = file.read().splitlines()
	indiceDivisaoRegras = linhas.index('')
	regras = linhas[:indiceDivisaoRegras]
	dicRegras = {campo.split(':')[0]:campo.split(':')[1].strip() for campo in regras} 
	for chave, valor in dicRegras.items():
		intervalos = valor.split(' or ')
		intervalos = [list(map(int,intervalo.split('-'))) for intervalo in intervalos]
		dicRegras[chave] = intervalos
	#dicRegras relaciona o campo aos seus intervalos da forma: {campo1:[[intervalo1],[intervalo2]], ....}.
	indiceDivisaoOutrosTickets = len(linhas) - list(reversed(linhas)).index('')
	seuTicket = linhas[indiceDivisaoRegras+1:indiceDivisaoOutrosTickets-1]
	seuTicket = seuTicket[-1]
	seuTicket = seuTicket.split(',')
	seuTicket = list(map(int,seuTicket))
	#seuTicket é uma lista de números representando seu ticket.
	ticketsProximos = linhas[indiceDivisaoOutrosTickets+1:]
	ticketsProximos = [ticket.split(',') for ticket in ticketsProximos]
	ticketsProximos = [list(map(int,ticket)) for ticket in ticketsProximos]
	#ticketsProximos é uma lista de listas representando os outros tickets.

somaCamposInvalidos = 0
ticketsInvalidos = set() #A parte 2 requer remover os tickets inválidos.
for ticket in ticketsProximos:
	for campo in ticket:
		campoPossivelmenteValido = False
		for intervalos in dicRegras.values():
			for intervalo in intervalos:
				if campo in range(intervalo[0],intervalo[1]+1):
					campoPossivelmenteValido = True #Em algum intervalo ele se encaixou.
		if not campoPossivelmenteValido:
			somaCamposInvalidos += campo
			ticketsInvalidos.add(tuple(ticket))
print("Taxa de erro no escaneamento de tickets:", somaCamposInvalidos)

#Parte 2:
ticketsValidos = [ticket for ticket in ticketsProximos if (tuple(ticket) not in ticketsInvalidos)]
numeroDeCampos = len(dicRegras)
dicionarioGabaritoCampos = {} #Dicionário que relaciona uma regra com o índice dela no campo.
while dicRegras:
	for campo, intervalos in dicRegras.items():
		indicesPlausiveis = []
		for indice in range(numeroDeCampos):
			if (indice not in dicionarioGabaritoCampos.values()): #Se já descobriu o gabarito deste indice nem tenta.
				indiceEhPlausivel = True #Armazena a informação para o índice específico.
				for ticket in ticketsValidos:
					campoPossivelmenteValido = False #Armazena a informação para este indice neste ticket.
					for intervalo in intervalos:
						if ticket[indice] in range(intervalo[0],intervalo[1]+1):
							campoPossivelmenteValido = True
					if not campoPossivelmenteValido:
						indiceEhPlausivel = False
				if indiceEhPlausivel:
					indicesPlausiveis.append(indice)
		if len(indicesPlausiveis) == 1:
			dicionarioGabaritoCampos[campo] = indicesPlausiveis[0]
	dicRegras = {campo:intervalos for campo,intervalos in dicRegras.items() if campo not in dicionarioGabaritoCampos} #Remove do dicionário os campos que já foram descobertos o "gabarito".
multiplicacaoDosCamposComDeparture = 1
for campo, indice in dicionarioGabaritoCampos.items():
	if 'departure' in campo:
		multiplicacaoDosCamposComDeparture *= seuTicket[indice]
print('Multiplicação dos valores do seu ticket referentes aos campos com "departure":', multiplicacaoDosCamposComDeparture)
