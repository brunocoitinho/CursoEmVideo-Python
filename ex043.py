print('Calculadora de IMC\n')
p = float(input('Digite o peso em Kg: '))
a = float(input('Digite a altura em metros: '))

imc = p / (a * a)

if imc < 18.5:
    cat = 'Abaixo do Peso'
elif imc <= 25:
    cat = 'Peso ideal'
elif imc <= 30:
    cat = 'Sobrepeso'
elif imc <= 40:
    cat = 'Obesidade'
else:
    cat = 'Obesidade Mórbida'

print('\nIMC: {}\nCondição: {}.'.format(imc, cat))