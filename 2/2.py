#Desafio do dia 02/12/2020
#a) Receber um numero mínimo e máximo de uma letra específica que a senha precisa ter e verificar se se encaixa.
#b) Idem, só que os numeros ditam qual posição da senha requer que um caracter esteja.
with open("input.txt") as file:
	linhas = file.read().splitlines()

numeroDeSenhasQueAtendeOCriterio = 0
numeroDeSenhasQueAtendemAoSegundoCriterio = 0
for linha in linhas:
	secoes = linha.split()
	regra = secoes[0]
	intervaloOcorrenciasNecessario = list(map(int,regra.split("-")))
	letraRequisitada = secoes[1][0]
	senha = secoes[2] #A senha em questão	
	numeroOcorrencias = 0 #Conta quantas vezes a letra aparece na senha
	for letra in senha:
		if letra == letraRequisitada:
			numeroOcorrencias+=1
	if numeroOcorrencias>=intervaloOcorrenciasNecessario[0] and numeroOcorrencias <= intervaloOcorrenciasNecessario[1]:
		numeroDeSenhasQueAtendeOCriterio+=1
	if (senha[intervaloOcorrenciasNecessario[0]-1]==letraRequisitada) ^ (senha[intervaloOcorrenciasNecessario[1]-1] == letraRequisitada):
		numeroDeSenhasQueAtendemAoSegundoCriterio+=1 

print("Numero de senhas que atendem ao primeiro critério:", numeroDeSenhasQueAtendeOCriterio)
print("Numero de senhas que atendem ao segundo critério:", numeroDeSenhasQueAtendemAoSegundoCriterio)
