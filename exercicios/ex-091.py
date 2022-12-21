from operator import itemgetter
from random import randint
from time import sleep

jogador = {
    'jogador_1': randint(1, 6),
    'jogador_2': randint(1, 6),
    'jogador_3': randint(1, 6),
    'jogador_4': randint(1, 6)
}
ranking = dict()
for k, v in jogador.items():
    print(f'O {k} tirou {v}.')
    sleep(0.5)
ranking = sorted(jogador.items(), key=itemgetter(1), reverse = True)
#print('-'*30)
print('-'* 5,  'RANKING', '-'*5)
for x, y in enumerate(ranking):
    print(f'{x+1}º lugar: {y[0]} com {y[1]}.')
    sleep(1)
