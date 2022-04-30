lista = list()
op = 'S'
valor = 0

while True:
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print('Este valor já foi digitado anteriormente e não será adcionado novamente a lista.')
    else:
        lista.append(valor)
    op = str(input('Deseja continuar digitando? [S/N]? '))
    while op not in 'SsNn':
        print('Valor inválido!')
        op = str(input('Deseja continuar digitando? [S/N]? '))
    if op in 'Nn':
        break

lista.sort()
print(f'\nOs números digitados foram {lista}')
