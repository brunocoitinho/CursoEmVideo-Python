times = ('Atletico - MG', 'Palmeiras', 'Fortaleza', 'Bragantino',
           'Flamengo', 'Athletico - PR', 'Atletico - GO', 'Ceara',
           'Internacional', 'Santos', 'Corinthians', 'Juventude',
           'Bahia', 'Sao Paulo', 'Fluminense', 'Cuiaba', 'Sport',
           'America - MG', 'Gremio', 'Chapecoense')


for c in range(0, len(times)):
    print(f'O nome do time {times[c].upper()} tem as seguintes vogais:  ', end='')
    for d in range(0, len(times[c])):
        if times[c][d] in 'AaEeIiOoUu':
            print(f'{times[c][d].lower()} ', end='')
    print('')



