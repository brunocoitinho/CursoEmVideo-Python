def aumentar(preco, acrescimo=0):
    return preco * (1 + (acrescimo / 100))


def diminuir(preco, reducao=0):
    return preco * (1 - (reducao / 100))


def dobra(preco):
    return preco * 2


def metade(preco):
    return preco / 2
