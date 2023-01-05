print('-'*45)
x = 'Alistamento'
print(f'{x:^45}')
print('-'*45)

from datetime import date

ano = int(input('Digite seu ano de nascimento: '))
print('-'*50)
atual = date.today().year
idade = atual - ano
if idade < 16:
    print(f'Você tem {idade} e ainda irá se alistar.')
elif 16 <= idade <= 18:
    print(f'Você tem {idade} e deve se alistar.')
else:
    print(f'Voce tem {idade} e já passou da idade de se alistar.')
print('-'*50)
