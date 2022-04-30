def leiaint(txt):
    while True:
        i = str(input(txt)).replace(' ', '')
        if i.isnumeric():
            i = int(i)
            break
        elif i.startswith('-'):
            i = i.strip('-')
            if i.isnumeric():
                i = int(i) * -1
                break
            else:
                print('\033[0;31mErro! Digite um número inteiro!\033[m')
        else:
            print('\033[0;31mErro! Digite um número inteiro!\033[m')
    return i


n = leiaint('Digite um número Inteiro: ')

print(f'O numero digitado foi {n}!')
