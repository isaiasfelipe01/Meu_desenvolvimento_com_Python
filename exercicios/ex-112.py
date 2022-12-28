def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mErro: por favor digite um número válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[031mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[031mErro: porfavor digite um número real válido\033[m!!!')
            continue
        except(KeyboardInterrupt):
            print('\n\033[031mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n

num1 = leiaInt('Digite um valor inteiro: ')
num2 = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {num1} e o valor real digitado foi {num2}')
