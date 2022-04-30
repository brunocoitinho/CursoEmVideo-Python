from ex109 import moeda

p = float(input('Digite o preço: R$'))
metade = moeda.metade(p)
dobro = moeda.dobra(p, True)
aumentado = moeda.aumentar(p, 10, False)
diminuido = moeda.diminuir(p, 13, False)

print(f'A metade de R${moeda.moeda(p)} é R${metade}')
print(f'O dobro de R${moeda.moeda(p)} é R${dobro}')
print(f'Aumentando 10%, temos R${aumentado}')
print(f'Reduzindo 13%, temos R${diminuido}')
