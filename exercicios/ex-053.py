print('-'*45)
x = 'Políndromo.'
print(f'{x:^45}')
print('-'*45)

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso= junto[::-1]
print(f'O inverso de {frase} é {inverso}')
if inverso == junto:
    print('Temos um políndromo.')
else:
    print('A frase não forma um políndromo.')
