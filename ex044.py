v = float(input('Valor do produto: '))
forma = int(input('Qual é a forma de pagamento\n'
                  '[ 1 ] A vista no dinheiro\n'
                  '[ 2 ] A vista no cartão\n'
                  '[ 3 ] A prazo\n'))
parc = int(input('Quantas parcelas: ')) if forma == 3 else print('')

if forma == 1:
    vf = v * 0.9
    parc = 1
elif forma == 2:
    vf = v * 0.95
    parc = 1
elif forma == 3:
    if parc < 2:
        print('Número inválido de parcelas')
    elif parc == 2:
        vf = v
    else:
        vf = v * 1.20
else:
    print('Opção inválida!')

print('Valor do produto: {:.2f}\n'
      'Quantidade de Parcelas:{}\n'
      'Valor da Parcela:{:.2f}\n'
      'Valor final: {:.2f}'.format(v, parc, vf/parc, vf))
