pessoas = list()
dados = dict()
soma = media = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO, digite M ou F.')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    pessoas.append(dados.copy())
    while True:
        slc = str(input('Quer continuar? [S/N] ')).upper()[0]
        if slc in 'NS':
            break
        print('ERRO')
    if slc == 'N':
        break
print('--'*30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
media = soma/len(pessoas)
print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in pessoas:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end=',')
print()
print('D) Lista de pessoas que estão acima da média: ', end='')
for p in pessoas:
    if p['idade'] >= media:
        print('     ')
        for x, y in p.items():
            print(f'{x} = {y} ', end='')
        print()
print('-'*30)
