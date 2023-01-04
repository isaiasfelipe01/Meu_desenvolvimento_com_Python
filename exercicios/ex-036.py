print('-'*45)
x = 'Aprovação de financiamento!'
print(f'{x:^45}')
print('-'*45)

valor = float(input('Qual valor do  imóvel? R$'))
salário = float(input('Qual salário do comprador? R$'))
ano = int(input('Em quantos anos deseja pagar o imóvel? '))

s1 = (salário*30)/100
pmt = valor/(ano*12)

if pmt <= s1:
    y = (f'O financiamento poderá ser aprovado com prestações mensais de {pmt:.2f} menstais.')
else:
    y = (f'O financiamento não poderá ser aprovado pois as parcelas de {pmt:.2f} são superiores ao mínimo de acordo com seu salário de {salário:.2f}!')

print('-'*len(y))
print(y)
print('-'*len(y))
    
    
    