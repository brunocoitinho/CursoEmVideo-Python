def escreva(txt):
    tam = len(txt)
    print('~' * (tam + 4))
    print(f'  {txt:^{tam}}  ')
    print('~' * (tam + 4))

def contador(ini, fim, passo):
    if passo == 0:
        passo = 1

    passo = int((passo ** 2) ** (1/2))

    print('=-=' * 11)
    print(f'Contagem de {ini} até {fim} de {passo} em {passo}:')
    print('=-=' * 11)

    if ini <= fim:
        for c in range(ini, fim + 1, passo):
            print(f'{c}...')
    else:
        for c in range(ini, fim-1, -passo):
            print(f'{c}...')

    print('Fim!')
    print('=-=' * 11)

contador(1, 10, 1)

contador(10, 0, 2)

i = int(input('Digite o valor inicial: '))
f = int(input('Digite o valor final: '))
p = int(input('Digite o passo: '))

print('')
contador(i, f, p)
