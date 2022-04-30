def area(l, c):
    print(f'Seu terreno {l:.2f}x{c:.2f} tem {l*c:.2f} m²')


print('Controle de Terreno')
print('_'*30)

larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))

area(larg, comp)
