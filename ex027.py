nome = str(input('Digite o nome da pessoa: '))

nome_split = nome.split()
tam = int(len(nome_split))

print('O primeiro nome de {} é {} e o último é {}.'.format(nome, nome_split[0], nome_split[tam-1]))
