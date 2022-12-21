def mult(a, b):
    x = a*b
    print(f'A área de um terreno {a:.2f}x{b:.2f} é de {x:.2f}m^2.')


print(' CONTROLE DE TERRENOS ')
print('-'*22)
largura = float(input('Largura(m): '))
comprimento = float(input('Comprimento (m): '))
mult(largura, comprimento)
