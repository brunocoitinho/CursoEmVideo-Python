import math

a = float(input('Digite o ângulo: '))
sena = math.sin(math.radians(a))
cosa = math.cos(math.radians(a))
tana = math.tan(math.radians(a))

print('O angulo de {}º possui seno igual a {:.2f}, cosseno igual a {:.2f} e tangente igual a {:.2f}.'.format(a, sena, cosa, tana))
