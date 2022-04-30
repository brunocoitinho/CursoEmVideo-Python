num = [[], [], []]
valor = 0

for r in range(0, 3):
    for c in range(0, 3):
        valor = int(input(f'Digite o valor da {c + 1}ª coluna da linha {r + 1}: '))
        num[r].append(valor)

for r in range(0, 3):
    print('')
    for c in range(0, 3):
        print(f'|{num[r][c]:^5} |', end='')

print('')