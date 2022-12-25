núm = int(input('Digite um número para ver a tabuada dele: '))

for c in range(0, 10):
    print(f'{núm} x {c + 1:2} = {núm * (c+1):2}')
