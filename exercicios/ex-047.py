print('-'*45)
x = 'Números pares'
print(f'{x:^45}')
print('-'*45)

for c in range(1, 51):
    if c % 2 == 0:
        print(c, end='-')