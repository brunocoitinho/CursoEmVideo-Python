import math

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h = math.sqrt((co ** 2) + (ca ** 2))

print('A hipotenusa é igual a {}.'.format(h))
