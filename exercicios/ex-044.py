print('-'*45)
x = 'Calculando preço!'
print(f'{x:^45}')
print('-'*45)

preço = float(input('Qual valor do produto? R$'))
print('''
[1] À vista no dinheiro;
[2] À vista no cartão;
[3] 2x no cartão;
[4] 3x ou mais no cartão.
''')

escolha = int(input('Qual forma de pagamento de acordo com as informações a cima? '))
print('-'* 60)

if escolha == 1:
    print('A forma de pagamento escolhida foi À VISTA!')
    valor = preço - ((preço * 10)/100)
    print(f'O valor R${preço:.2f} com 10% de desconto ficou de R${valor:.2f}')
if escolha  == 2:
    print('A forma de pagamento escolhida foi À VISTA NO CARTÃO!')
    valor = preço - ((preço * 5)/100)
    print(f'O valor R${preço:.2f} com 5% de desconto ficou de R${valor:.2f}')
if escolha == 3:
    print('A forma de pagamento escolhido foi 2x NO CARTÃO!')
    print(f'o valor do produto é de R${preço:.2f} dividido em 2x de R${(preço/2):.2f}')
if escolha == 4:
    print('A opção escolhida foi dividido em 3x ou mais vezes no cartão!')
    while True:
        parcelas = int(input('Digite um número de parcelas entre 3 e 12: '))
        if parcelas < 3:
            print('Número digitado incorreto! Tente novamente.')
            continue
        if 3 <= parcelas <= 12:
            break
        else:
            print('Incorreto! tente novamente')
            continue
    valor = preço + ((preço * 20)/100)
    y = (f'O valor R${preço:.2f} dividido no cartão em mais de 3x ficará de R${valor:.2f} com parcelas de R${valor/parcelas:.2f}')
    s = len(y)
    print('-'*s)
    print(y)
print('-'*s)
