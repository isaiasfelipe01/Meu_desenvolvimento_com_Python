from random import randint
from time import sleep

print('-=' * 15)
print('     NÚMEROS DA MEGA SENA     ')
print('-=' * 15)
lista = list()
jogos = list()
quant = int(input('Quantos jogos deseja fazer? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
for c in range(1, 4):
    print('.')
    sleep(1)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(0.3)
print('-=' * 5, 'BOA SORTE', '-=' * 5)
