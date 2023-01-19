print('-'*45)
x = 'Maior e menor peso.'
print(f'{x:^45}')
print('-'*45)

maior_peso = 0
menor_peso = 0
for c in range(0, 5):
    peso = float(input(f'Digite o {c+1}° peso: '))
    if maior_peso == 0:
        maior_peso = peso
    if menor_peso == 0:
        menor_peso = peso
    if peso > maior_peso:
        maior_peso = peso
    elif peso < menor_peso:
        menor_peso = peso
print('-'*45)
print(f'O maior peso é {maior_peso:.2f}Kg e o menor peso é {menor_peso:.2f}Kg.')
