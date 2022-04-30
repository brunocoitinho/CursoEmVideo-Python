def leiafloat(txt):
    while True:
        try:
            num = str(input(txt)).replace(' ', '')
            num = num.replace(',', '.', 1)
            if num.startswith('-'):
                num = num.strip('-')
                i = float(num) * -1
            else:
                i = float(num)
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar um número!\033[m')
            return 0.0
        except (ValueError, TypeError):
            print('\033[0;31mErro! Digite um número real!\033[m')
            continue
        else:
            break

    return i


def leiaint(txt):
    while True:
        try:
            num = str(input(txt)).replace(' ', '')
            if num.startswith('-'):
                num = num.strip('-')
                i = int(num) * -1
            else:
                i = int(num)
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar um número!\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[0;31mErro! Digite um número inteiro!\033[m')
            continue
        else:
            break

    return i


ni = leiaint('Digite um número Inteiro: ')
nf = leiafloat('Digite um número Real: ')


print(f'O numero inteiro digitado foi {ni} e o real foi {nf:.1f}!')
