ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
       'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
       'dezenove', 'vinte')

num = 0

while True:
    num = int(input('Digite um número inteiro entre 0 e 20: '))
    if 20 >= num >= 0:
        break
    else:
        print('Digite um valor válido!\n')

print(f'Você digitou o número {ext[num]}!')
