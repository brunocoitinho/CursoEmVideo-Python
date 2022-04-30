n = int(input('Digite um número: '))
p = 0
for c in range(n-1, 1, -1):
    if n % c == 0:
        p = 1
if p > 0:
    print("O número {} não é primo".format(n))
else:
    print("O número {} é primo".format(n))
