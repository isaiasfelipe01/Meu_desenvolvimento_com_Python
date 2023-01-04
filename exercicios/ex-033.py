print('-'*45)
x = 'Maior e menor número.'
print(f'{x:^45}')
print('-'*45)

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
    
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
    
print(f'O menor número é {menor}.')
print(f'O maior número é {maior}.')
