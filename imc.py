def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input('Digite seu peso em KG: '))
altura = float(input('Digite sua altura em metros: '))
imc = calcular_imc(peso, altura)

print('Seu IMC é {:.2f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 24.9:
    print('Você está saudavel!')
elif 25 <= imc < 29.9:
    print('Você está com sobrepeso!')
else:
    print('Você está obeso!')
