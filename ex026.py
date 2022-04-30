frase = str(input('Digite uma frase: '))

qtda = frase.lower().count('a')
posini = frase.lower().find('a')
posfin = frase.lower().rfind('a')

print(
    'A letra A aparece {} vezes na frase digitada, sendo pela primeira vez na posição {} e pela última vez na posição {}.'.format(
        qtda, posini, posfin))
