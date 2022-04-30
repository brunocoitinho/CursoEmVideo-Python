valor = float(input('Qual é o valor da casa? '))
sal = float(input('Qual é o salário do comprador? '))
t = float(input('Em quantos anos pretende pagar? '))

prest = valor / t / 12

print('\nValor da prestação: R${:.2f}'.format(prest))
print('Limite mensal do comprador: R${:.2f}\n'.format(sal*0.3))


if prest > sal*0.3:
    print('Empréstimo Negado!')
else:
    print('Empréstimo Aprovado!')


