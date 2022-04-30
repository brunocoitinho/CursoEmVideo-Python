stats = list()
jogador = dict()
gols = list()
totalgols = 0
op = ''
cod = -1

while True:
    jogador['nome'] = str(input('Jogador: '))
    jogador['partidas'] = int(input('Total de partidas jogadas: '))

    for g in range(0, jogador['partidas']):
        gols.append(int(input(f'Total de gols na {g + 1}ª partida: ')))
        totalgols += gols[g]

    jogador['gols'] = gols[:]
    jogador['total'] = totalgols
    totalgols = 0

    stats.append(jogador.copy())

    gols.clear()

    print()

    op = str(input('Deseja continuar [S/N]? '))


    while op not in 'SsNn':
        print('Valor inválido')
        op = str(input('Deseja continuar [S/N]? '))

    print('<==>'*10)
    print()

    if op in 'Nn':
        break

print('-'*40)
print(f'{"LISTA DE JOGADORES":^40}')
print('-'*40)
print(f'{"cod":<5}', end='')
print(f'{"nome":<15}', end='')
print(f'{"gols":<15}', end='')
print(f'{"total":<5}')
print('-'*40)


for j in range(0, len(stats)):
    print(f'{j:<5}{stats[j]["nome"]:<15}{str(stats[j]["gols"]):<15}{stats[j]["total"]}')

print('-'*30)

while True:
    cod = int(input('Digite o código do jogador para mais dados ou 999 para encerrar: '))

    while cod != 999 and cod > len(stats)-1:
        print('Valor inválido!')
        cod = int(input('Digite o código do jogador para mais dados ou 999 para encerrar: '))

    if cod == 999:
        break

    print('<==>' * 10)

    print(f'O jogador {stats[cod]["nome"]} jogou {stats[cod]["partidas"]} partidas.')

    for g in range(0, stats[cod]['partidas']):
        print(f'=> Na {g + 1}ª partida ele fez {stats[cod]["gols"][g]}. ')

    print(f'\nTotal de gols marcados: {stats[cod]["total"]}')
    print(f'Média de gols por jogo: {stats[cod]["total"]/ stats[cod]["partidas"]:.2f}\n')

