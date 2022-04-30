prod = ('Maça', 6.60, 'Banana', 12.50, 'Abacaxi', 2.20)

print('=-=' * 15)
print(f'{"Listagem de Preços":^30}')
print('=-=' * 15)

for c in range(0, len(prod)):
    if c % 2 == 0:
        print(f'{prod[c]:.<30}R$', end='')
    else:
        print(f'{prod[c]:>7.2f}')

print('=-=' * 15)
