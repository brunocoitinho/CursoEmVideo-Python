print('Seja bem vindo ao banco X!')

valor = 0.0

ced50 = 0
ced20 = 0
ced10 = 0
ced1 = 0

valor = int(input('Quando você deseja sacar? [Notas disponíveis 1, 10, 20, 50] \nR$ '))

vf = float(valor)

print(f'Você sacou: R${vf:.2f}')

while True:
    if valor >= 50:
        ced50 = valor // 50
        valor -= ced50*50
        print(f'Você sacou {ced50} notas de 50')
    elif valor >= 20:
        ced20 = valor // 20
        valor -= ced20*20
        print(f'Você sacou {ced20} notas de 20')
    elif valor >= 10:
        ced10 = valor // 10
        valor -= ced10*10
        print(f'Você sacou {ced10} notas de 10')
    elif valor >= 1:
        ced1 = valor
        valor -= ced1
        print(f'Você sacou {ced1} notas de 1')
    else:
        break
