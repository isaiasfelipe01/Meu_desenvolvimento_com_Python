print('-'*45)
x = 'Contagem regressiva'
print(f'{x:^45}')
print('-'*45)

from time import sleep

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('BUM!!!')
