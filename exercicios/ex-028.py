from random import randint
from time import sleep

print('='*30)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('='*30)

ns = randint(0, 5)
ne = int(input('Em qual número eu pensei? '))

print(f'PROCESSANDO...')
sleep(2)

if ns == ne:
    print(f'Acertou!!! Parabens, você conseguiu me vencer.')
else:
    print(f'Errou!!! O número que eu pensei foi {ns} e não {ne}')
