def fatorial(num=1, show=False):
    """
    -> Cálcula o fatorial da função
    :param num: Fatorial a ser calculado
    :param show: (opcional) Define se o cálculo será retornado ou só o resultado
    :return: resultado ou cálculo + resultado
    """
    fat = 1
    txt = ''
    for c in range(num, 1, -1):
        fat *= c
        if show:
            txt += f'{c} x '
    if show:
        txt += f'1 = {fat}'
    else:
        txt = fat
    return txt


print(fatorial(5, True))
