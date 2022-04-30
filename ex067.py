n = 0
while True:
    n = int(input('Digite o número que você deseja ver a tabuada (digite um valor negativo para encerrar): '))
    if n < 0:
        break

    print(f"\nTabuada de {n}")

    for c in range(1, 11, 1):
        print(f"{n} x {c} = {n*c}")
    print("")

