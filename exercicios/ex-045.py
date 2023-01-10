print('-'*45)
x = 'Jokenpô.'
print(f'{x:^45}')
print('-'*45)

from random import randint

j = ('Pedra', 'Papel', 'Tesoura')
cpu = randint(0, 2)
cpu1 = j[cpu]
print('''
[1] Pedra
[2] Papel
[3] Tesoura
''')
jogador = int(input('Qual você escolhe? '))

print('-'*45)
if cpu == jogador:
    print('EMPATE!')
elif cpu == 0 and jogador == 2:
    jogador = 'Papel'
    print(f'Jogador GANHOU! \nVocê escolheu {jogador} e o computador {cpu1}.')
elif cpu == 0 and jogador == 3:
    jogador = 'Tesoura'
    print(f'Computador GANHOU! \nVocê escolheu {jogador} e o computador {cpu1}.')
elif cpu == 1 and jogador == 1:
    jogador = 'Pedra'
    print(f'Computaor GANHOU! \nVocê escolheu {jogador} e o computador {cpu1}.')
elif cpu == 1 and jogador == 3:
    jogador = 'Tesoura'
    print(f'Jogador GANHOU! \nVocê escolheu {jogador} e o computador {cpu1}.')
elif cpu == 2 and jogador == 1:
    jogador = 'Pedra'
    print(f'Jogador GANHOU! \nVocê escolheu {jogador} e o computador {cpu1}.')
elif cpu == 2 and jogador == 2:
    jogador = 'Papel'
    print(f'Computador GANHOU! \nVocê escolheu {jogador} e o computador {cpu1}.')
else:
    print('REINICIE O PROGRAMA!!')
print('-'*45)
