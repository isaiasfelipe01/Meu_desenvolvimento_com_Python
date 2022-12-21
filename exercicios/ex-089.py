ficha = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    pergunta = str(input('Quer continuar? [S/N] ')).upper()
    if pergunta == 'N':
        break
print('-=' * 30)
print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>7.1f}')
while True:
    print('-' * 30)
    opc = int(input('Mostrar notas de qual aluno(a)? (999 interrompe) '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'As notas do(a) aluno(a) {ficha[opc] [0]} são {ficha[opc] [1]}')
print('VOLTE SEMPRE')
