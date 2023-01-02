print('-'*30)
x = 'Ano bisexto.'
print(f'{x:^30}')
print('-'*30)

from datetime import date

ano = int(input('Qual ano quer analizar? Digite 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 == 0 or ano % 400 == 0:
    print(f'O ano {ano} é bisexto!')
else:
    print(f'O ano {ano} não é bisexto!')
