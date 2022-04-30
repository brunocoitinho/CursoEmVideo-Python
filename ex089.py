turma = list()
aluno = list()
notas = list()
op1 = ''
op2 = 0

while True:
    aluno.append(str(input('Nome: ')))
    notas.append(float(input('1ª Nota: ')))
    notas.append(float(input('2ª Nota: ')))
    aluno.append(notas[:])
    notas.clear()
    turma.append(aluno[:])
    aluno.clear()

    op1 = str(input('Deseja inserir mais um aluno? [S/N]? '))
    while op1 not in 'SsNn':
        print('Valor inválido!')
        op1 = str(input('Deseja inserir mais um aluno? [S/N]? '))
    if op1 in 'Nn':
        break

print('\n Deseja exibir o boletim de qual aluno?')

print('0 - Todos')

for a in range(0, len(turma)):
    print(f'{a + 1} - {turma[a][0]}')

while True:

    op2 = int(input())

    while op2 not in range(0, len(turma) + 1):
        print('Valor inválido!')
        op2 = int(input('Deseja exibir o boletim de qual aluno?\n'))

    print('=' * 40)
    print('Boletim')
    print('=' * 40)
    print(f'{"No.":<4}{"Nome":<10}{"Nota 1":<10}{"Nota 2":<10}{"Média":<10}')

    if op2 == 0:
        for a in range(0, len(turma)):
            print(f'{a+1:<4}{turma[a][0]:<10}{turma[a][1][0]:<10}{turma[a][1][1]:<10}{(turma[a][1][0] + turma[a][1][1]) / 2:<10}')
        break;
    else:
        print(f'{op2:<4}{turma[op2 -1][0]:<10}{turma[op2 -1][1][0]:<10}{turma[op2 -1][1][1]:<10}{(turma[op2 -1][1][0] + turma[op2 -1][1][1]) / 2:<10}')
        break
