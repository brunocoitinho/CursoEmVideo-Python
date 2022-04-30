v = float(input('Qual é a velocidade do carro em Km/h: '))

print('O carro está a {:.2f}Km/h.'.format(v))

if v > 80:
    print('Você foi multado!')
    print('O valor da multa é R${:.2f}.'.format((v-80)*7))

