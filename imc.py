#Começamos definindo uma função
def calcular_imc(peso, altura):
    #Aqui colocamos a formula do IMC que é: peso / (altura * altura)
    imc = peso / (altura ** 2)
    return imc
#Solicitamos os dados do paciente em questão
peso = float(input('Digite seu peso em KG: '))
altura = float(input('Digite sua altura em metros: '))
imc = calcular_imc(peso, altura)

print('Seu IMC é {:.2f}'.format(imc))
#E por ultimo damos um diagnóstico de acordo com os cálculos feitos.
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 24.9:
    print('Você está saudavel!')
elif 25 <= imc < 29.9:
    print('Você está com sobrepeso!')
else:
    print('Você está obeso!')
