import random

print('Vamos jogar Jokenpo!')

p1 = int(input('Escolha a sua mão\n'
               '[ 1 ] Pedra\n'
               '[ 2 ] Papel\n'
               '[ 3 ] Tesoura\n'))

p2 = random.randint(1, 3)
resultado = 'deve escolher uma das opções indicadas.'

if p2 == 1:
    cpu = 'pedra'
elif p2 == 2:
    cpu = 'papel'
else:
    cpu = 'tesoura'


print('O computador escolheu {}.\n'.format(cpu))

if p1 == p2:
    resultado = 'empatou!'
elif p1 == 1:
    if p2 == 2:
        resultado = 'perdeu!'
    elif p2 == 3:
        resultado = 'ganhou!'
elif p1 == 2:
    if p2 == 1:
        resultado = 'ganhou!'
    elif p2 == 3:
        resultado = 'perdeu!'
elif p1 == 3:
    if p2 == 1:
        resultado = 'perdeu!'
    elif p2 == 2:
        resultado = 'ganhou!'
else:
    print('Opção inválida!')

print('Você {}'.format(resultado))
