print('-'*45)
x = 'calculando aluguel de carro.'
print(f'{x:^45}')
print('-'*45)

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
diaria = dias * 60
rodado = km * 0.15
print(f'O total a pagar é R${diaria+rodado:.2f}.')
