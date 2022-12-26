import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade do preço R${moeda.moeda(p)} é R${moeda.moeda(moeda.metade(p))}.')
print(f'O dobro de R${moeda.moeda(p)} é R${moeda.moeda(moeda.dobro(p))}.')
print(f'Aumentando o preço{moeda.moeda(p)} em 10%, temos R${moeda.moeda(moeda.aumentar(p, 10))}.')
