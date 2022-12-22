def fatorial(n, show=False):
    """
    -> Calcular o fatorial de  um númer:
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end ='')
        f *= c
    return f


fat = int(input('Qual número deseja fatorar -> '))
a1 = str(input('Tecle "A" para resultado e cálculo / Tecle "B" para somente resultado. \n-> ')).upper()
if a1 == 'A':
    asd = True
elif a1 == 'B':
    asd = False
else:
    print('ERRO, Algo deu errado, reinicie o programa!')

#print(fatorial(fat, show=asd))
help(fatorial)