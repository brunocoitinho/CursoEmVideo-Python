def aumentar(preco=0, acrescimo=0, f=True):
    if f:
        return moeda(preco * (1 + (acrescimo / 100)))
    else:
        return preco * (1 + (acrescimo / 100))


def diminuir(preco=0, reducao=0, f=True):
    if f:
        return moeda(preco * (1 - (reducao / 100)))
    else:
        return preco * (1 - (reducao / 100))


def dobra(preco=0, f=True):
    if f:
        return moeda(preco * 2)
    else:
        return preco * 2


def metade(preco=0, f=True):
    if f:
        return moeda(preco / 2)
    else:
        return preco / 2


def moeda(preco=0):
    return f'{preco:.2f}'.replace('.', ',')


def resumo(preco=0, acrescimo=0, reducao=0, f=True):
    print('-' * 40)
    print(f'{"Resumo de Valor":^40}')
    print('-' * 40)
    print(f'Preço analisado: \tR${moeda(preco)}')
    print(f'Dobro do preço: \tR${dobra(preco, f)}')
    print(f'Metade do preço: \tR${metade(preco, f)}')
    print(f'{acrescimo}% de aumento:  \tR${aumentar(preco,acrescimo, f)}')
    print(f'{reducao}% de redução:  \tR${diminuir(preco,reducao, f)}')
    print('-' * 40)
