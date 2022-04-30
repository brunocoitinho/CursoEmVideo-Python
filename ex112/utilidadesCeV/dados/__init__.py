def leiaDinheiro(texto=''):
    while True:
        din = input(f'{texto}').replace(',', '.', 1)
        if din.replace('.', '', 1).isnumeric():
            break
        else:
            print(f'\033[31mErro! "{din}" é um preço inválido!\033[m')

    return float(din)
