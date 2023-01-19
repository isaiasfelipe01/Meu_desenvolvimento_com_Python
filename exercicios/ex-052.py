print('-'*45)
x = 'Número primo.'
print(f'{x:^45}')
print('-'*45)

num = int(input('Digite um número: '))
if num == 2 or num == 3 or num == 5:
    print('É um número primo')
elif num % 2 == 0 or num % 3 ==0 or num % 5 == 0:
    print('Não é um número primo')
else:
    print('É um número primo')

