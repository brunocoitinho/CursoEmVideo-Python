listanum = list()
num = 0

for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0:
        listanum.append(num)
        print('Adicionado na posição 0.')
    else:
        for pos, val in enumerate(listanum):
            if num <= listanum[pos]:
                listanum.insert(pos, num)
                print(f'Adicionado na posição {pos}.')
                break
            elif pos == len(listanum)-1:
                listanum.append(num)
                print(f'Adicionado na posição {len(listanum)-1}.')
                break

print(listanum)




