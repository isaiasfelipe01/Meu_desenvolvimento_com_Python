print('-'*45)
x = 'Maior e menor idade.'
print(f'{x:^45}')
print('-'*45)

from datetime import date
data_atual = date.today().year
cont_maior = 0
cont_menor = 0
for c in range(0, 7):
    ano = int(input(f'Ano de nascimento da {c+1}° pessoa: '))
    idade = data_atual - ano
    if idade >= 18:
        cont_maior += 1
    else:
        cont_menor += 1
print('-'*71)
print(f'Ao total tivemos {cont_maior} pessoas com maior idade e {cont_menor} pessoas com menor idade.')
print('-'*71)
