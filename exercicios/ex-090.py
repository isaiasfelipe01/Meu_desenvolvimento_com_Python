dados = dict()
dados['Nome'] = str(input('Nome: '))
dados['Média'] = float(input(f'Média de {dados["Nome"]}: '))
if dados['Média'] >= 7:
    dados['situação'] = 'Aprovado'
elif 5 <= dados['Média'] < 7:
    dados['situação'] = 'Recuperação'
else:
    dados['situação'] = 'Reprovado'

for k, v in dados.items():
    print(f'{k} é igual a {v}')
