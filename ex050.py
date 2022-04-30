n = int(input('Digite um número: '))
s = 0

if n%2 == 0:
    s += n

for c in range(0, 5, 1):
    n = int(input('Digite mais um número: '))
    if n % 2 == 0:
        s += n

print("A soma dos pares digitados é {}.".format(s))
