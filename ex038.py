n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))

if n1 > n2:
    print('Resultado: {} é maior que {}.'.format(n1, n2))
elif n2 > n1:
    print('Resultado: {} é maior que {}.'.format(n2, n1))
else:
    print('Resultado: Ambos os números tem o mesmo valor que é {}.'.format(n1))
