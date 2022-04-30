import math

num = float(input('Digite um número entre 0 até 9999: '))
m = math.trunc(num / 1000)
c = math.trunc((num - (m * 1000))/100)
d = math.trunc((num - (m * 1000) - (c * 100))/10)
u = math.trunc(num - (m * 1000) - (c * 100) - (d * 10))

print('Milhares: {}\nCentenas: {}\nDezenas: {}\nUnidades: {}'.format(m, c, d, u))
