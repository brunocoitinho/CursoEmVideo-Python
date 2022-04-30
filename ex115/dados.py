def leiaidade(txt):
    while True:
        try:
            num = str(input(txt)).replace(' ', '')
            if num.startswith('-'):
                print('\033[0;31mErro! Digite uma idade válida!\033[m')
                continue
            else:
                i = int(num)
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar um número!\033[m')
            return -1
        except (ValueError, TypeError):
            print('\033[0;31mErro! Digite uma idade válida!!\033[m')
            continue
        else:
            break

    return i
