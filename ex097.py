def escreva(txt):
    tam = len(txt)
    print('~' * (tam + 4))
    print(f'  {txt:^{tam}}  ')
    print('~' * (tam + 4))


escreva('Bruno Coitinho Pereira')
