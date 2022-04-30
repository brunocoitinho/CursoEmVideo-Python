def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    """
    -> Define se a pessoa está apta a votar
    :param ano: Ano de Nascimento
    :return: Condição de votação
    """
    if idade < 16:
        return f'Com {idade} de idade o voto NÃO É PERMITIDO.'
    elif idade < 18 or idade >= 65:
        return f'Com {idade} de idade o voto é OPCIONAL.'
    else:
        return f'Com {idade} de idade o voto é OBRIGATÓRIO'


print('-'*40)
anoNascimento = int(input('Digite o seu ano de nascimento: '))
print(voto(anoNascimento))
print('-'*40)

