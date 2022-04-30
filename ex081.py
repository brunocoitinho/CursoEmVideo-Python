lista = list()
op = 'S'
valor = 0
nope = ''

while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    op = str(input('Deseja continuar digitando? [S/N]? '))
    while op not in 'SsNn':
        print('Valor inválido!')
        op = str(input('Deseja continuar digitando? [S/N]? '))
    if op in 'Nn':
        break

lista.sort(reverse=True)

print(f'Números digitados: {len(lista)}\n')
print(f'\nOs números digitados foram {lista}')

if 5 not in lista:
    nope = 'não '

print(f'O número 5 {nope}é um deles')

