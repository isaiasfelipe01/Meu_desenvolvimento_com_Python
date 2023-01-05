from datetime import date

atual = date.today().year
ano = int(input('Digite o ano de nascimento: '))
idade = atual - ano
if idade <= 9:
    print(f'Você tem {idade} anos e se encaixa no perfil MIRIM!')
elif 9 < idade <= 14:
    print(f'Você tem {idade} anos e se encaixa no perfil INFANTIL!')
elif 14 < idade <= 19:
    print(f'Você tem {idade} anos e se encaixa no perfil JUNIOR!')
elif 19 < idade <= 25:
    print(f'você tem {idade} anos e se encaixa no perfil SÊNIOR!')
else:
    print(f'Você tem {idade} anos e se encaixa no perfil MASTER!')