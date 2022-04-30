from ex108 import moeda

p = float(input('Digite o preço: R$'))
metade = moeda.moeda(moeda.metade(p))
dobro = moeda.moeda(moeda.dobra(p))
aumentado = moeda.moeda(moeda.aumentar(p, 10))
diminuido = moeda.moeda(moeda.diminuir(p, 13))

print(f'A metade de R${moeda.moeda(p)} é R${metade}')
print(f'O dobro de R${moeda.moeda(p)} é R${dobro}')
print(f'Aumentando 10%, temos R${aumentado}')
print(f'Reduzindo 13%, temos R${diminuido}')
