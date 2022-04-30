import random
np = nc = -1
po = - 1
c = 0

while True:
    print('\nVamos jogar par ou impar?\n')

    po = int(input('Qual vai ser o resultado? (Digite 1 para impar ou 2 para par):  '))
    while po < 1 or po > 2:
        print('Numero inválido!')
        po = int(input('Qual vai ser o resultado? (Digite 1 para impar ou 2 para par):  '))

    np = int(input('Digite um número de 0 a 10: '))
    while np < 0 or np > 10:
        print('Numero inválido!')
        np = int(input('Digite um número de 0 a 10: '))

    nc = random.randint(0, 10)
    print(f'\nO computador escolheu {nc}!\n')

    if (np + nc) % 2 == 0 and po == 2:
        print('Você venceu! Jogue mais uma!')
        c += 1
        print(f'{c}ª vitória')
    elif (np + nc) % 2 != 0 and po == 1:
        print('Você venceu! Jogue mais uma!')
        c += 1
        print(f'{c}ª vitória')
    else:
        print(f'Você perdeu!\nTotal de vitórias: {c}')
        break
