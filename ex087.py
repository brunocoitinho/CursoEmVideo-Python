num = [[], [], []]
valor = 0
somapar = 0
somacol3 = 0

for r in range(0, 3):
    for c in range(0, 3):
        valor = int(input(f'Digite o valor da {c + 1}ª coluna da linha {r + 1}: '))
        if valor % 2 == 0:
            somapar += valor
        if c == 2:
            somacol3 += valor
        num[r].append(valor)

for r in range(0, 3):
    print('')
    for c in range(0, 3):
        print(f'|{num[r][c]:^5} |', end='')

print(f'\n\nSoma dos pares: {somapar}')
print(f'Soma da terceira coluna: {somacol3}')
print(f'Maior valor da 2ª linha: {max(num[1])}')

