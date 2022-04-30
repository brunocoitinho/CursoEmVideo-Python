nome = ''
preco = 0.0
sexo = ''
op = 's'
total = 0.0
qtdprodutos = 0
maisdemil = 0
maisbarato = ''
maisbaratopreco = 0.0

print('\nDigite os items')

while True:
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    while preco < 0:
        print('\nDigite um preco válido!\n')
        preco = float(input('Preço: R$ '))
    print('')
    total += preco
    qtdprodutos += 1
    if preco > 1000:
        maisdemil += 1

    if qtdprodutos == 1:
        maisbarato = nome
        maisbaratopreco = preco

    elif maisbaratopreco > preco:
        maisbarato = nome
        maisbaratopreco = preco



    op = str(input('Deseja continuar? [S/N] '))
    while op not in 'SsNn':
        print('\nDigite uma das opções disponíveis!\n')
        op = str(input('Deseja continuar? [S/N] '))
    if op in 'Nn':
        break

print(f'\nTotal de Gastos: R$ {total:.2f}')
print(f'Quantidade de produtos acima de R$1000.00: {maisdemil}')
print(f'Produto mais barato: {maisbarato} por R$ {maisbaratopreco:.2f}')

