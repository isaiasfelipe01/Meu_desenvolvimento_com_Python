dados = dict()
partida = list()
dados['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range(0, tot):
    partida.append(int(input(f'Quantos gols na partida {c+1}? ')))
dados['gols'] = partida[:]
dados['total'] = sum(dados['gols'])
print('--'*27)
print(dados)
print('--'*27)
for x, y in dados.items():
    print(f'O campo {x} temo o valor {y}.')
print('--'*25)
print(f'O jogador {dados["nome"]} jogou {tot} partidas.')
for x, y in enumerate(dados['gols']):
    print(f'    ->Na partida {x}, fez {y} gols.')
print(f'Foi um total de {sum(partida)} gols.')
