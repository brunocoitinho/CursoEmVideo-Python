print('Conversor de bases')
num = int(input('Digite o número inteiro que você deseja converter: '))
choice = int(input('Agora escolha a basa para conversão\n'
                   'Digite 1 - Para Binário\n'
                   'Digite 2 - Para Octal\n'
                   'Digite 3 - Para Hexadecimal\n'))

if choice == 1:
    print('Resultado: {}'.format(bin(num)))
elif choice == 2:
    print('Resultado: {}'.format(oct(num)))
elif choice == 3:
    print('Resultado: {}'.format(hex(num)))
else:
    print('Opção inválida!')
