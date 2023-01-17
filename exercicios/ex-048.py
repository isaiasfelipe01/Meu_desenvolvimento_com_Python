print('-'*45)
x = 'Soma números ímpares'
print(f'{x:^45}')
print('-'*45)

contador = 0
soma = 0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        contador += 1
        soma += c

print(f'A soma dos {contador} valores é igual a {soma}.')
print('-'*45)