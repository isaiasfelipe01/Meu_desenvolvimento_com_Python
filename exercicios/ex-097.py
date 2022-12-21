def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


n = str(input('Digite o nome: '))
escreva(n)
