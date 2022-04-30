nome = ''
idade = 0
sexo = ''
op = 's'
maior18 = 0
totalhomem = 0
mulhermenor20 = 0

while True:
    print('\n Digite os dados cadastrais.')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    while idade < 0:
        print('\nDigite uma idade válida!\n')
        idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F/O]: '))
    while sexo not in 'MmFfOo':
        print('\nDigite uma das opções disponíveis!\n')
        sexo = str(input('Sexo[M/F/O]: '))

    if idade > 18:
        maior18 += 1
    if sexo in 'Mm':
        totalhomem += 1
    if sexo in 'Ff' and idade < 20:
        mulhermenor20 += 1

    op = str(input('Deseja continuar? [S/N] '))
    while op not in 'SsNn':
        print('\nDigite uma das opções disponíveis!\n')
        op = str(input('Deseja continuar? [S/N] '))
    if op in 'Nn':
        break

print(f'\nTotal de pessoas com mais de 18 anos: {maior18}')
print(f'Total de homens: {totalhomem}')
print(f'Total de mulheres com menos de 20 anos: {mulhermenor20}')

