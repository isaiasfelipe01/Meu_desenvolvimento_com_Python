print('-'*60)
x = 'Calculando aumento de acordo com o salário.'
print(f'{x:^60}')
print('-'*60)

salário = float(input('Salário do funcionário: R$'))
if salário <= 1250:
    a = ((salário*15)/100)
    print(f'O aumento foi de R${a:.2f} e somado ao salário ficou R${(a+salário):.2f}.')
else:
    a = (salário*10)/100
    print(f'O aumento foi de R${a:.2f} e somando ao salário ficou R${(a+salário):.2f}.')
