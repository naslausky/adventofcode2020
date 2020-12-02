#Desafio do dia 02/12/2020
#a) Receber um numero minimo e máximo de uma letra especifica que a senha precisa ter e verificar se se encaixa.
#b) Idem, só que os numeros ditam qual posicao da senha requer que um caracter esteja.
with open("input.txt") as file:
	linhas = file.read().splitlines()

numeroDeSenhasQueAtendeOCriterio = 0
numeroDeSenhasQueAtendemAoSegundoCriterio = 0
for linha in linhas:
	secoes = linha.split()
	regra = secoes[0]
	intervaloOcorrenciasNecessario = list(map(int,regra.split("-")))
	letraRequisitada = secoes[1][0]
	#A senha em questão
	senha = secoes[2]
	#Conta quantas vezes a letra aparece na senha
	numeroOcorrencias = 0
	for letra in senha:
		if letra == letraRequisitada:
			numeroOcorrencias+=1
	if numeroOcorrencias>=intervaloOcorrenciasNecessario[0] and numeroOcorrencias <= intervaloOcorrenciasNecessario[1]:
		numeroDeSenhasQueAtendeOCriterio+=1
	if (senha[intervaloOcorrenciasNecessario[0]-1]==letraRequisitada) ^ (senha[intervaloOcorrenciasNecessario[1]-1] == letraRequisitada):
		numeroDeSenhasQueAtendemAoSegundoCriterio+=1 

print("Numero de senhas que atendem ao primeiro critério:")
print(numeroDeSenhasQueAtendeOCriterio)

print("Numero de senhas que atendem ao segundo critério:")
print(numeroDeSenhasQueAtendemAoSegundoCriterio)
