n1 = int(input('Digite 1º número: '))
n2 = int(input('Digite 2º número: '))
op = 0

while op != 5:
    print('Digite o número correspondente a operação desejada:')
    print('[1] - Soma\n[2] - Multiplicação\n[3] - Qual é o maior?')
    op = int(input('[4] - Digitar novos números\n[5] - Sair do programa\n'))
    if op != 5:
        if op == 1:
            print('A soma dos números é {}.'.format(n1 + n2))
        elif op == 2:
            print('O produto dos números é {}.'.format(n1 * n2))
        elif op == 3:
            print('O maior número é {}.'.format(max(n1, n2)))
        elif op == 4:
            n1 = int(input('Digite 1º número: '))
            n2 = int(input('Digite 2º número: '))
        else:
            print('Valor inválido')

print('\nFim')


