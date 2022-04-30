print('Somatório de valores: ')

n = 0
qtd = 0
sumnum = 0

while n != 999:
    qtd += 1
    sumnum += n
    n = int(input('Digite um valor inteiro pra ser somado ou 999 para ver o resultado: '))

if n == 999:
    qtd -= 1

print('Total de números: {}\nSoma dos números: {}'.format(qtd, sumnum))
