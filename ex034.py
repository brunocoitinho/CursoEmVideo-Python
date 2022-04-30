s = float(input('Digite é o salário do funcionário: '))

if s > 1250:
    print('O novo salário é R${:.2f}.'.format((s * 1.1)))
else:
    print('O novo salário é R${:.2f}.'.format((s * 1.15)))
