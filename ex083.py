exp = str(input('Digite uma expressão matemática: '))
pa = 0
pf = 0

for c in range(0, len(exp)):
    if exp[c] == '(':
        pa += 1
    if exp[c] == ')':
        pf += 1
    if pf > pa:
        print('Você não fechou os parenteses abertos.')
        break
    if c == len(exp)-1:
        if pa > pf:
            print('Você não fechou os parenteses abertos.')
        else:
            print('Expressão sem problemas.')

