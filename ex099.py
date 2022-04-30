from time import sleep

def maior(*num):

    print('=-='*35)
    print('Analisando os numeros informados', end='')
    sleep(1)
    print('.', end='')
    sleep(1)
    print('.', end='')
    sleep(1)
    print('.')
    sleep(1)
    print(f'Total de números informados: {len(num)}')
    sleep(1)
    if len(num) > 0:
        print('Os números informados são:{', end='')
        c = 0
        ma = num[0]
        for n in num:
            if n > ma:
                ma = n
            if c < len(num)-1:
                print(f'{n}, ', end='')
                c += 1
            else:
                print(f'{n}', end='')
            sleep(0.5)
        print('}')
        print(f'O maior número é {ma}!')
    else:
        print('Não há número maior!')
    print('=-=' * 35)


maior(4, 5, 2, 8)
