import random

lista = list()
for c in range(1, 5):
    lista.append(str(input(f'{c}° aluno: ')))
a = random.choice(lista)
print(f'O aluno escolhido foi {a}')
