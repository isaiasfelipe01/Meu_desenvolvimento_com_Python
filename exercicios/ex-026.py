frase = str(input('Digite uma frase: ')).strip().upper()

print('A letra A aparerce {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}.'.format(frase.find('A')))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')))
