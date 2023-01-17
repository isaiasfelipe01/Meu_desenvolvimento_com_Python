print('-'*45)
x = 'Soma de números pares'
print(f'{x:^45}')
print('-'*45)

soma = 0
for c in range(0, 6):
    num = int(input(f'Digite o {c+1}° número: '))
    if num % 2 == 0:
        soma += num
print('-'*45)
print(f'A soma dos valores pares digitados é {soma}.')
