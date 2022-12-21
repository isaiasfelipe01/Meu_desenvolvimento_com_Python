num = list()
par = list()
impares = list()
while True:
    num.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? [S/N] ')).upper()
    if resp == 'N':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impares.append(v)

print('=-'*30)
print(f'A lista digitada completa é: {num}')
print(f'A lista de números par é {par}.')
print(f'A lista de números ímpares é {impares}.')
