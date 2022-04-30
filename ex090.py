aluno = dict()

aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input('Digite a média do aluno: '))

if aluno['media'] < 7:
    aluno['status'] = 'Reprovado'
else:
    aluno['status'] = 'Aprovado'

print('='*30)
print('Situação do aluno')
print('='*30)

print(f'{"Nome":<20}{"Média":<10}{"Situação":<20}')
print(f'{aluno["nome"]:<20}{aluno["media"]:<10}{aluno["status"]:<20}')

