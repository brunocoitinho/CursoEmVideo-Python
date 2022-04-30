grupo = list()
pessoa = list()
leves = list()
pesados = list()

while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    grupo.append(pessoa[:])
    if len(grupo) == 1:
        leves.append(pessoa[:])
        pesados.append(pessoa[:])
    else:
        if pessoa[1] == leves[0][1]:
            leves.append(pessoa[:])
        elif pessoa[1] < leves[0][1]:
            leves.clear()
            leves.append(pessoa[:])
        if pessoa[1] == pesados[0][1]:
            pesados.append(pessoa[:])
        elif pessoa[1] > pesados[0][1]:
            pesados.clear()
            pesados.append(pessoa[:])

    pessoa.clear()

    op = str(input('Deseja continuar digitando? [S/N]? '))
    while op not in 'SsNn':
        print('Valor inválido!')
        op = str(input('Deseja continuar digitando? [S/N]? '))
    if op in 'Nn':
        break

print(f'\nTotal de cadastros: {len(grupo)}')

print(f'Individuos mais pesados ({pesados[0][1]:.2f} Kg): ', end='')

for c in range(0, len(pesados)):
    print(f'{pesados[c][0]}', end='')
    if c == len(pesados) - 1:
        print('.')
    elif c == len(pesados) - 2:
        print(' e ', end='')
    else:
        print(', ', end='')

print(f'Individuos mais leves ({leves[0][1]:.2f} Kg): ', end='')

for c in range(0, len(leves)):
    print(f'{leves[c][0]}', end='')
    if c == len(leves) - 1:
        print('.')
    elif c == len(leves) - 2:
        print(' e ', end='')
    else:
        print(', ', end='')
