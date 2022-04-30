import math

a = int(input('Digite o primeiro lado do triangulo: '))
b = int(input('Digite o segundo lado do triangulo: '))
c = int(input('Digite o terceiro lado do triangulo: '))

print('')

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



