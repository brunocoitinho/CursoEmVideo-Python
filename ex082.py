listanum = list()
listapar = list()
listaimpar = list()

op = 'S'
valor = 0

while True:
    valor = int(input('Digite um valor: '))
    listanum.append(valor)
    if valor % 2 == 0:
        listapar.append(valor)
    else:
        listaimpar.append(valor)
    op = str(input('Deseja continuar digitando? [S/N]? '))
    while op not in 'SsNn':
        print('Valor inválido!')
        op = str(input('Deseja continuar digitando? [S/N]? '))
    if op in 'Nn':
        break

print(f'\nNúmeros digitados: {listanum}\nNúmeros Pares: {listapar}\nNúmeros Ímpares: {listaimpar}')