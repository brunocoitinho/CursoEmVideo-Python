from random import randint
from time import sleep


def sorteio(n):
    print('Sorteando 5 valores da lista: ', end='')
    sleep(0.5)
    for c in range(0, 5):
        n.append(randint(0, 9))
        print(n[c], end=' ')
        sleep(0.5)
    print()


def somaPar(n):
    soma = 0
    for c in range(0, len(n)):
        if n[c] % 2 == 0:
            soma += n[c]
    print(f'Somando os valores pares temos {soma}.')


num = list()
sorteio(num)
somaPar(num)
