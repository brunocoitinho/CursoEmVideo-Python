sumidade = 0
idadehomem = 0
nomehomem = ''
totalmulher20 = 0
i = 0

for i in range(0, 4, 1):
    print("{}ª pessoa".format(i+1))
    nome = str(input("Digite o nome: "))
    idade = int(input("Digite a idade: "))
    sexo = str(input("Digite o sexo [F/M/O]: ")).lower()
    print('\n')
    sumidade += idade
    if sexo == 'm' and idade > idadehomem:
        idadehomem = idade
        nomehomem = nome
    if sexo == 'f' and idade < 20:
        totalmulher20 += 1


print('\nA média de idade do grupo é {}.'.format(sumidade/(i+1)))
print('O homem mais velho se chama {} e a idade dele é {}.'.format(nomehomem, idadehomem))
print('Total de mulheres com menos de 20 anos: {}'.format(totalmulher20))
