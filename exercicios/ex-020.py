import random

lista = list()
for c in range(1, 5):
    lista.append(str(input(f'{c}° Aluno: ')))
random.shuffle(lista)
print(f'A ordem de apresentação será: \n{lista}')
