print('-'*45)
x = 'Tipo de triângulo!'
print(f'{x:^45}')
print('-'*45)

reta1 = float(input('Primeira reta: '))
reta2 = float(input('Segunda reta: '))
reta3 = float(input('Terceira reta: '))

print('-'*55)

if reta1 < reta2 + reta2 and reta2 < reta1 + reta3 and reta3 < reta2 + reta1:
    if reta1 == reta2 == reta3:
        print(f'Os segmentos citados formam um triângulo EQUILÁTERO!')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print(f'Os segmentos citados formam um triângulo ISÓSCELES')
    else:
        print('Os segmentos citados formam um triângulo ESCALENO!')
else:
    print('Os segmentos citados não formam triângulo!')
print('-'*55)
