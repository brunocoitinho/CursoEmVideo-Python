import random

pc = random.randint(0, 5)
print('Tente advinhar o número que o computador escolheu.')
player = int(input('Digite um número inteiro de 0 a 5: '))

print('O PC escolheu {}. Você chutou {}.'.format(pc, player))

if pc == player:
    print('Parabéns! Você acertou!')
else:
    print('Que pena! Você errou!')