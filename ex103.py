def ficha(nome='<desconhecido>', gols=0):
    """
    -> Ficha de cadastro de jogador
    :param nome: Nome do jogador
    :param gols: Gols marcados pelo jogador
    :return:
    """

    print(f'O jogador {nome} fez {gols} gols.')


print('-' * 40)
j = str(input('Nome do jogador: '))
g = input('Total de gols: ')


if j.isspace() or j == '':
    j = '<desconhecido>'


if str(g).isnumeric():
    g = int(g)
else:
    g = 0

ficha(j, g)
