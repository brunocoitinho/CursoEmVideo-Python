n = int(input('Digite quantos números você deseja ver: '))

while n < 1:
    print('Valor inválido!')
    n = int(input('Digite quantos números você deseja ver: '))
ultnum = 0
pun = 0
novultnum = 0

i = 0
while i < n:
    if i == 0:
        print(0, end='')
    elif i == 1:
        print(' -> ', 1, end='')
        pun = ultnum
        ultnum = 1
    else:
        print(' -> ', ultnum + pun, end='')
        novultnum = ultnum + pun
        pun = ultnum
        ultnum = novultnum
    i += 1

