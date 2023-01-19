print('-'*45)
x = 'Progressão Aritmética.'
print(f'{x:^45}')
print('-'*45)

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
print('-'*45)
print('Os 10 primeiros termos da PA são:')
print('  ->', primeiro_termo, end=' ')
for c in range(1, 10):
    termos = primeiro_termo+(razao*c)
    print(termos, end=' ')
