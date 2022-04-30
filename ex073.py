classif = ('Atlético - MG', 'Palmeiras', 'Fortaleza', 'Bragantino',
           'Flamengo', 'Athletico - PR', 'Atlético - GO', 'Ceará',
           'Internacional', 'Santos', 'Corinthians', 'Juventude',
           'Bahia', 'São Paulo', 'Fluminense', 'Cuiabá', 'Sport',
           'América - MG', 'Grêmio', 'Chapecoense')

print('\nOs cinco primeiros times são:')
for pos, time in enumerate(classif[:5]):
    print(f'{pos+1}º- {time}')

print('\nOs quatro últimos são:')
for pos, time in enumerate(classif[-4:]):
    print(f'{pos+17}º- {time}')

print(f'\nOrdem Alfabetica: {sorted(classif)}')

chap = classif.index('Chapecoense')+1
print(f'\nA Chape está em {chap}° lugar.')

