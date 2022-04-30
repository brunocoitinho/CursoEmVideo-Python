import ex115.cadastro as cadastro

while True:
    opt = cadastro.chamamenu()
    if opt == 1:
        cadastro.mostracadastro()
    if opt == 2:
        cadastro.novocadastro()
    if opt == 3:
        print('-' * 50)
        print(f'{"Saindo do sistema... Até logo!":^50}')
        print('-' * 50)
        break
