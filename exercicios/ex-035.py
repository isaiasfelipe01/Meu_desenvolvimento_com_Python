print('-'*45)
x ='Analizando triângulos.'
print(f'{x:^45}')
print('-'*45)

reta1 = float(input('Primeiro segmento do triângulo: '))
reta2 = float(input('Segundo segmento do triângulo:'))
reta3 = float(input('Terceiro segmento do triângulo: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os segmentos acima formam um triângulo.')
else:
    print('Os segmentos acima não formam um triângulo.')
    