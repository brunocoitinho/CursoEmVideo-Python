nome = str(input('Digite o nome da pessoa: '))

silva = str(nome.lower().find('silva') != -1)

print('Esta pessoa{}tem o sobrenome Silva.'.format(
    silva.replace('True', ' ').replace('False', ' não ')))
