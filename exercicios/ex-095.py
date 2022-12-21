dados = dict()
time = list()
partida = list()
while True:
    dados.clear()
    dados['nome'] = str(input('Nome do jogador: '))
    quant = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    partida.clear()
    for c in range(0, quant):
        partida.append(int(input(f'Quantos gols na partida {c+1}: ')))
    dados['gols'] = partida[:]
    dados['total'] = sum(partida)
    time.append(dados.copy())
    while True:
        selc = str(input('Deseja continuar: [S/N] ')).upper()[0]
        if selc in 'SN':
            break
        print('ERRO, tente novamente!!')
    if selc in 'N':
        break
print('-'*55)
print('Nº ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-'*55)
for x, y in enumerate(time):
    print(f'{x:>1} ', end='')
    for d in y.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*55)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print('Erro!')
    else:
        print(f'Levantamento do jogador {time[busca]["nome"]}: ')
        for x, y in enumerate(time[busca]['gols']):
            print(f'    No jogo {x+1} fez {y} gols.')
    print('-'*55)
print('acaboouuu')
