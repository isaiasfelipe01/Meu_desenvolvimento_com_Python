num = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N]')).upper()
    if r in 'N':
        break
print('=-'*30)
num.sort()
print(f'Você digitou os valores {num}.')
print('=-'*30)
