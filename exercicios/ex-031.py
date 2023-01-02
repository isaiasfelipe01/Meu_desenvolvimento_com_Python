print('-'*59)
x = 'Calculando o valor da viagem de acordo com a distância.'
print(f'{x:^60}')
print('-'*59)

km = float(input('Qual a distancia percorrida: '))
if km < 200:
    valor = km * 0.50
    print(f'O valor da sua viagem ficou de R${valor:.2f}.')
else:
    valor = km * 0.45
    print(f'O valor da sua viagem ficou de R${valor:.2f}'.replace('.', ','), '.')
