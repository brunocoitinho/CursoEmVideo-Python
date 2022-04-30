nome = str(input('Digite seu nome completo: '))

ma = nome.upper().strip()
mi = nome.lower().strip()

qtd = len(nome)-nome.count(' ')
nome_split = nome.split()
qtdprim = len(nome_split[0])-nome_split[0].count(' ')

print('Seu nome é: {}\n Caixa Alta: {}\n Caixa Baixa: {}\n Qtd. de Letras no 1º nome: {}\n Qtd. de letras total:{} '.format(nome, ma, mi, qtdprim, qtd))