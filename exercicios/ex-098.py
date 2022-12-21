from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-'*30)
    print(f'Contagemde {i} até {f} de {p} em {p}.')
    sleep(3)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!!')


contador(0, 10, 2)
contador(10, 0, 2)
print('-'*25)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início:  '))
fim = int(input('Fim:     '))
pas = int(input('Passo:   '))
contador(ini, fim, pas)
