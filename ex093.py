jogador = dict()
gols = list()
totalgols = 0

jogador['nome'] = str(input('Jogador: '))
jogador['partidas'] = int(input('Total de partidas jogadas: '))

for g in range(0, jogador['partidas']):
    gols.append(int(input(f'Total de gols na {g+1}ª partida: ')))

jogador['gols'] = gols

print()

print('<==>'*10)

print(f'\nO jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.\n')

for g in range(0, jogador['partidas']):
    print(f'=> Na {g+1}ª partida ele fez {gols[g]}. ')
    totalgols += gols[g]

print(f'\nTotal de gols marcados: {totalgols}')
print(f'Média de gols por jogo: {totalgols/jogador["partidas"]:.2f}')


