import math

a = float(input('Digite um ângulo que você deseja: '))
seno = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tg = math.tan(math.radians(a))
print(f'O ângulo de {a}° tem \n Seno de {seno:.2f} \n Cosseno de {cos:.2f} \n Tangente de {tg:.2f}')
