from math import sqrt

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacenete: '))
hp = sqrt((co*co) + (ca*ca))
print(f'A hipotenusa mede {hp:.2f}.')
