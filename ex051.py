p = int(input('Digite o primeiro termo da P.A.: '))
r = int(input('Digite a razão da P.A.: '))

for c in range(1, 11, 1):
    print("{} - : {}".format(c, p + (c-1) * r))
