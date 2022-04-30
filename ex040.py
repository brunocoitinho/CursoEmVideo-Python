print('Calculadora de média final')
n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota:'))

media = (n1 + n2) / 2
print('A média do aluno é {}.\n'.format(media))

if media < 5:
    print('Aluno reprovado.')
elif 5 <= media < 7:
    print('Aluno em recuperação.')
else:
    print('Aluno aprovado!')
