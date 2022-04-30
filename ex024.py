nome = str(input('Digite o nome da cidade: '))

nome_split = nome.split()

print('O nome da cidade começa com Santo? {}.'.format(
    str(nome_split[0] == 'Santo').replace('True', 'Sim').replace('False', 'Não')))
