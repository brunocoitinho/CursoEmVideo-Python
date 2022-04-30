num = (int(input('Digite um número de 0 a 9: ')),
       int(input('Digite um número de 0 a 9: ')),
       int(input('Digite um número de 0 a 9: ')),
       int(input('Digite um número de 0 a 9: ')))

par = 0

print(f'Lista: {num}')
print(f'O total de vezes que o número 9 apareceu é {num.count(9)} ')
if 3 in num:
    print(f'A primeira vez que o número 3 apareceu é na posição {num.index(3)}')
else:
    print('O número 3 não foi digitado')

print('Lista de números pares digitados: (', end='')


for c in range(0, len(num)):
    if c > 0:
        if num[c] % 2 == 0:
            print(', ', end='')
            print(f'{num[c]}', end='')
    elif num[c] % 2 == 0:
        print(f'{num[c]}', end='')
print(')')
