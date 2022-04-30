import datetime

ano = int(input('Qual é o ano de nascimento do atleta? '))

idade = datetime.date.today().year - ano

if idade < 10:
    cat = 'Mirim'
elif idade < 15:
    cat = 'Infantil'
elif idade < 20:
    cat = 'Junior'
elif idade < 21:
    cat = 'Senior'
else:
    cat = 'Master'

print('O Atleta tem {} anos e a sua categoria é {}.'.format(idade, cat))
