import random

pc = random.randint(0, 10)
print('\nTente advinhar o número que o computador escolheu.')
player = int(input('Digite um número inteiro de 0 a 10: '))

tent = 1

while pc != player:
    print('Que pena! Você errou!\n')
    tent += 1
    player = int(input('Digite outro número inteiro de 0 a 10: '))

print('Parabéns! Você acertou na {}ª tentativa!'.format(tent))
