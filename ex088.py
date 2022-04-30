from random import randint
from time import sleep
qtd = int(input('Quantas apostas você quer gerar? '))

jogos = list()
aposta = list()
valor = 0

print('-'*20)
print('Jogos da Mega Sena')
print('-'*20)

for c in range(0,qtd):
    for d in range(0,6):
        while True:
            valor = randint(1, 60)
            if valor not in aposta:
                break
        aposta.append(valor)
    jogos.append(aposta[:])
    aposta.clear()

for a in jogos:
    print(a)
    sleep(1)

