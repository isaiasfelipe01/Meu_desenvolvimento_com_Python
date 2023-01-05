print('-'*45)
x = 'Aprovado, reprovado, recuperação!'
print(f'{x:^45}')
print('-'*45)

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Sefunda nota: '))
print('-'*45)
média = (nota1+nota2)/2

if média < 5:
    print(f'Sua média é {média:.2f} e você está REPROVADO!'.replace('.', ','))
elif 5 <= média < 7:
    print(f'Sua média é {média:.2f} e você está em RECUPERAÇÃO!'.replace('.', ','))
else:
    print(f'Sua média é {média:.2f} e você está APROVADO!'.replace('.', ','))
print('-'*45)
