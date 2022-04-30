km = float(input('Quantos KM o carro percorreu? '))
dia = float(input('Por quantos dias o carro foi alugado? '))

p = (60 * dia) + (0.15 * km)

print('O total a pagar é de R${:.2f}'.format(p))