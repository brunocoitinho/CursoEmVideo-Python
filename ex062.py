p = int(input('Digite o primeiro termo da P.A.: '))
r = int(input('Digite a razão da P.A.: '))

c = 1
while c < 10:
    print("{} - : {}".format(c, p + (c-1) * r))
    c += 1

print('Deseja ver mais alguns termos?')
op = int(input('Digite a qtd ou 0 para sair\n'))

c += 1
while op != 0:
    ci = c
    while c < ci + op:
        print("{} - : {}".format(c, p + (c - 1) * r))
        c += 1
    print('Deseja ver mais alguns termos?')
    op = int(input('Digite a qtd ou 0 para sair\n'))

print('\nFim!\n')