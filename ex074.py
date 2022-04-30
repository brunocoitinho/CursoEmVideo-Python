import random

num = (random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9))


print(f'Lista: {num}')
print(f'O maior número é {max(num)}')
print(f'O menor número é {min(num)}')
