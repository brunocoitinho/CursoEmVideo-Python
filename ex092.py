from datetime import date
from sys import exit

trabalhador = {}

while True:
    trabalhador['nome'] = str(input('Digite o nome do trabalhador: '))
    trabalhador['ano'] = int(input('Digite o ano de nascimento do trabalhador: '))
    trabalhador['idade'] = date.today().year - trabalhador['ano']
    trabalhador['ctps'] = int(input('Digite o num. da carteira de trabalho (0 se não tiver): '))
    if trabalhador['ctps'] == 0:
        break
    trabalhador['anocontrato'] = int(input('Digite o ano de contratação do trabalhador: '))
    trabalhador['salario'] = float(input('Digite o salário do trabalhador: '))
    trabalhador['idadeaposentadoria'] = trabalhador['anocontrato'] + 35 - date.today().year + trabalhador['idade']
    break


print(f'\nNome: {trabalhador["nome"]}')
print(f'Nascido em {trabalhador["ano"]}({trabalhador["idade"]} anos)')

if trabalhador['ctps'] == 0:
    print('O trabalhador não possui carteira de trabalho.')
    exit()

print(f'CTPS nº {trabalhador["ctps"]}')
print(f'Salário: R${trabalhador["salario"]:.2f}')
print(f'Entrou na empresa em {trabalhador["anocontrato"]}.')
print(f'Vai se aposentar com {trabalhador["idadeaposentadoria"]}.')



print(trabalhador)
