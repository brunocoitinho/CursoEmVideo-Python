import ex115.dados as dados


def chamamenu():
    while True:
        print('-' * 50)
        print(f'{"MENU PRINCIPAL":^50}')
        print('-' * 50)
        print(f'\033[0;34m{1}\033[m - \033[0;33m{"Ver pessoas cadastradas"}\033[m')
        print(f'\033[0;34m{2}\033[m - \033[0;33m{"Cadastrar nova pessoa"}\033[m')
        print(f'\033[0;34m{3}\033[m - \033[0;33m{"Sair do sistema"}\033[m')
        print('-' * 50)
        try:
            op = int(input('Sua opção: '))
            if 3 >= op > 0:
                return op
            else:
                print('\033[0;31mOpção inválida!\033[m')
        except (ValueError, TypeError):
            print('\033[0;31mOpção inválida!\033[m')
            continue


def mostracadastro():
    print('-' * 50)
    print(f'{"PESSOAS CADASTRADAS":^50}')
    print('-' * 50)
    try:
        with open('ex115/banco.txt', 'r') as banco:
            conteudo = banco.read()
        print(conteudo)
    except FileNotFoundError:
        print('Nenhuma pessoa cadastrada')


def novocadastro():
    print('-' * 50)
    print(f'{"NOVO CADASTRO":^50}')
    print('-' * 50)
    nome = str(input('Nome: '))
    idade = dados.leiaidade('Idade: ')
    with open('ex115/banco.txt', 'a') as banco:
        banco.write(f'{nome}\t\t\t\t\t{idade} anos')
    print(f'Registro de {nome} foi cadastrado! ')
