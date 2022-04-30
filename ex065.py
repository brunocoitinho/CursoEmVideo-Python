n = 0
qtd = 0
sumnum = 0
op = ''
ma = me = 0

while op.lower() != 'n':
    qtd += 1
    sumnum += n
    n = int(input('Digite um valor inteiro: '))
    if qtd == 1:
        ma = me = n
    else:
        ma = max(n, ma)
        me = min(n, me)
    op = str(input('Deseja continuar [S/N]: '))
    while op.lower() not in 'sn':
        print('Digite um valor válido!')
        op = str(input('Deseja continuar [S/N]: '))


print('Total de números: {}\nMédia: {}\n Maior: {}\n Menor: {}'.format(qtd, sumnum / qtd, ma, me ))
