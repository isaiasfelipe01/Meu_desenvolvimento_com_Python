def  ficha(a=0, b=0):
    if a == '':
        a = '<desconhecido>'
    print(f'O jogador {a} fez {b} gol(s) na partida.')


nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
ficha(nome, gols)
