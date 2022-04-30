p = int(input('Digite o primeiro termo da P.A.: '))
r = int(input('Digite a razão da P.A.: '))

c = 1
while c < 10:
    print("{} - : {}".format(c, p + (c-1) * r))
    c += 1
