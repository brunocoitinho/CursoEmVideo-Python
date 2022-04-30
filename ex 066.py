n = s = c = 0
while True:
    n = int(input('Digite um número (999 para encerrar): '))
    if n == 999:
        break
    s += n
    c += 1

print(f'O total de números digitados foi {c}. A soma deles vale {s}.')
