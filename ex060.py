print('Calculadora de Fatorial')
n = int(input('Digite o número: '))
ni = n

fat = 0

if n == 0 or n == 1:
    fat = 1
else:
    fat = 1
    while n != 1:
        fat = fat * n
        n -= 1

print('{}! = {}'. format(ni, fat))
