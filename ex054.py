from datetime import date
ano_atual = date.today().year
ano = int(input('Digite o ano de nascimento: '))
ma = 0
me = 0

if ano_atual - ano >= 18:
    ma += 1
else:
    me += 1

for c in range(0, 6, 1):
    ano = int(input('Digite o ano de nascimento: '))
    if ano_atual - ano >= 18:
        ma += 1
    else:
        me += 1

print("\nTotal de pessoas: {}\nMaiores de idade: {}\nMenores de idade: {}".format(ma+me, ma, me))
