lista = list()
maior = -1
menor = -1
posmenor = list()
posmaior = []

for c in range(0,5):
    lista.append(int(input('Digite um valor: ')))
    if c == 0:
        maior = menor = lista[c]
        posmaior.append(c)
        posmenor.append(c)
    else:
        if lista[c] > maior:
            maior = lista[c]
            for p in range(0, len(posmaior)):
                posmaior.pop()
            posmaior.append(c)
        elif lista[c] == maior:
            posmaior.append(c)
        if lista[c] < menor:
            menor = lista[c]
            for p in range(0, len(posmenor)):
                posmenor.pop()
            posmenor.append(c)
        elif lista[c] == menor:
            posmenor.append(c)

print(f'O maior número é {maior} na posição {posmaior}.')
print(f'O menor número é {menor} na posição {posmenor}.')

