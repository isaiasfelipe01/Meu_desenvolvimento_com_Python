print('-'*45)
x = 'Qual valor maior!'
print(f'{x:^45}')
print('-'*45)

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

print('-'*45)
if valor1 > valor2:
    print(f'O primeiro valor é maior.')
elif valor2 > valor1:
    print(f'O segundo valor é maior.')
else:
    print(f'Os valores são iguais.')
print('-'*45)
