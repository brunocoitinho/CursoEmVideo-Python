import math

a = int(input('Digite o primeiro lado do triangulo: '))
b = int(input('Digite o segundo lado do triangulo: '))
c = int(input('Digite o terceiro lado do triangulo: '))

print('')

pos = 1 # 1 indica que é possível fazer um triangulo

if math.fabs(b - c) < a and a < b + c:
    print('É possível fazer um triangulo com esses lados.')
else:
    if math.fabs(a - c) < b and a < b + c:
        print('É possível fazer um triangulo com esses lados.')
    else:
        if math.fabs(a - b) < c and c < b + a:
            print('É possível fazer um triangulo com esses lados.')
        else:
            print('Não é possível fazer um triangulo com esses lados.')
            pos = 0

if  pos == 1:
    if a == b == c:
        print('E ele é equilátero.')
    elif a != b != c:
        print('E ele é escaleno.')
    else:
        print('E ele é isósceles.')