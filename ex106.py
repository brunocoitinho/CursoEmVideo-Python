from time import sleep

def escreva(txt, estilo=''):
    tam = len(txt)
    estilofim = ''
    if estilo != '':
        estilofim = '\033[m'
        estilo = '\033[' + estilo + 'm'
    print(f'{estilo}', end='')
    print(f'~' * (tam + 4))
    print(f'  {txt:^{tam}}  ')
    print(f'~' * (tam + 4))
    print(f'{estilofim}', end='')

def ajuda(comando):
    escreva(f'Acessando o manual do comando {comando}', '0;39;44')
    sleep(2)
    print('\033[7;39;40m', end='')
    help(comando)
    print('\033[m', end='')
    sleep(2)


while True:
    escreva('Sistema de Ajuda PyHelp', '0;39;42')
    h = str(input('Função ou Biblioteca > '))
    if h == 'fim'.lower():
        escreva(f'Até logo', '0;39;41')
        break
    ajuda(h)

