print('-'*45)
x = 'Tabuada'
print(f'{x:^45}')
print('-'*45)

mult = int(input('Qual número deseja multiplicar? '))
print('-'*45)
for c in range(1, 11):
    resp = c * mult
    print(f'{c:>2} X {mult:>2} = {resp:>3}')
print('-'*15)
