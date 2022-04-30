import datetime

ano = int(input('Qual é o seu ano de nascimento? '))

idade = datetime.date.today().year - ano

if idade < 17:
    print('Fica tranquilo. Faltam {} anos para você se alistar.'.format(18 - idade))
elif idade == 17:
    print('Fica tranquilo. Falta 1 ano para você se alistar.')
elif idade == 18:
    print('VOCÊ TEM QUE SE ALISTAR ESSE ANO!!!!')
elif idade == 19:
    print('Velho demais. Se você não se alistou há 1 ano atrás já era.')
else:
    print('Velho demais. Se você não se alistou há {} anos atrás já era.'.format(idade - 18))
