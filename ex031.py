d = float(input('Digite é a distância da viagem em Km: '))

if d <= 200:
    print('O valor da passagem é R${}.'.format(str(d * 0.5).replace('.', ',')))
else:
    print('O valor da passagem é R${}.'.format(str((200 * 0.5) + ((d - 200) * 0.45)).replace('.', ',')))
