listap = list()
pessoa = dict()
op = ''
sumidade = 0
listam = list()
listaveio = list()
aux = dict()

while True:
    pessoa['nome'] = str(input('Digite o nome da pessoa: '))
    pessoa['sexo'] = str(input('Digite o sexo da pessoa [F/M/O]: '))

    while pessoa['sexo'] not in 'FfMmOo':
        print('Valor inválido')
        pessoa['sexo'] = str(input('Digite o sexo da pessoa [F/M/O]: '))

    pessoa['idade'] = int(input('Digite a idade: '))

    while pessoa['idade'] < 0:
        print('Valor inválido')
        pessoa['idade'] = int(input('Digite a idade: '))

    sumidade += pessoa['idade']

    listap.append(pessoa.copy())

    if pessoa['sexo'] in 'Ff':
        listam.append(pessoa.copy())

    op = str(input('Deseja continuar [S/N]? '))

    while op not in 'SsNn':
        print('Valor inválido')
        op = str(input('Deseja continuar [S/N]? '))

    print('<==>'*10)
    print()

    if op in 'Nn':
        print()
        break

media = sumidade/len(listap)

for i in range(0, len(listap)):
    if listap[i]['idade'] > media:
        listaveio.append(listap[i].copy())

print(f'Total de de pessoas digtadas: {len(listap)}')
print(f'A média de idade do grupo é {media:.2f} anos')

print()
if len(listam) > 0:
    print('Lista de mulheres digitadas: ')
    for i in range (0, len(listam)):
        print(f'{i+1} - {listam[i]["nome"]}')
else:
    print('Não foram digitados dados de mulheres.')

print()
if len(listaveio) > 0:
    print('Lista de pessoas mais velhas que a média: ')
    for i in range (0, len(listaveio)):
        print(f'{i+1} - {listaveio[i]["nome"]}')
else:
    print('Não foram digitadas pessoas mais velhas que a média.')




