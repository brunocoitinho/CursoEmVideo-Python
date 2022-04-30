
peso = int(input('Digite o peso da pessoa 1: '))
ma = peso
me = peso

for c in range(0, 4, 1):
    peso = int(input('Digite o peso da pessoa {}: '.format(c+2)))
    if peso > ma:
        ma = peso
    elif peso < me:
        me = peso

print("\nTotal de pessoas: {}\nMaior Peso: {}\nMenor Peso: {}".format(c+2, ma, me))
