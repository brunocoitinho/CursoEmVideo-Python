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
