s = str(input('Digite o sexo da pessoa [S/M/O] : '))

while s not in 'MmFfOo':
    print('Valor inválido!')
    s = str(input('Digite o sexo da pessoa: '))

print('\nFim!')
