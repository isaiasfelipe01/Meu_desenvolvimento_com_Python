print('-'*60)
x = 'Transformando um número em binário, octal, hexadecimal.'
print(f'{x:^60}')
print('-'*60)

núm = int(input('Digite um número inteiro: '))
print('''Digite um número inteiro: 
    [1] converter para binário
    [2] converter para octal
    [3] converter para hexadecimal''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{núm} convertido para binário {bin(núm)[2:]}.')
elif opção == 2:
    print(f'{núm} convertido para octal {oct(núm)[2:]}.')
else:
    print(f'{núm} convertido para hexadecimal {hex(núm)[2:]}.')
