n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
n3 = int(input('Digite mais um número inteiro: '))

if n1 > n2 and n1 > n3:
    print('O primeiro é o maior!')
else:
    if n2 > n1 and n2 > n3:
        print('O segundo é o maior!')
    else:
        if n3 > n1 and n3 > n2:
            print('O terceiro é o maior!')
        else:
            print('Não existe um único número maior!')

if n1 < n2 and n1 < n3:
    print('O primeiro é o menor!')
else:
    if n2 < n1 and n2 < n3:
        print('O segundo é o menor!')
    else:
        if n3 < n1 and n3 < n2:
            print('O terceiro é o menor!')
        else:
            print('Não existe um único número menor!')


