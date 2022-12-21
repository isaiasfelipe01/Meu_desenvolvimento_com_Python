maior = menor = 0
dado = []
principal = []

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        elif dado[1] < menor:
            menor = dado[1]
    principal.append(dado[:])
    dado.clear()
    resp = str(input('Deseja continuar? [S/N] ')).upper()
    if resp == 'N':
        break

print(f'Ao todo você cadastrou {len(principal)} pessoas.')
print(f'O maior peso foi {maior:.2f}Kg. Peso de : ', end='')
for p in principal:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print('.')
print(f'O menor peso foi {menor:.2f}Kg. Peso de : ', end='')
for p in principal:
    if p[1] == menor:
        print(f'{p[0]} ', end='')
print('.')
