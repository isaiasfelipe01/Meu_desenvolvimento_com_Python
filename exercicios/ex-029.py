km = int(input('Velocidade atual do carro: '))

if km > 80:
    calc = (km-80)*7
    print(f'MULTADO!!! Você ultrapassou o limite de velocidadde!\nVocê foi multado no valor de R${calc},00.')
else:
    print('Tenha um bom dia! Dirija com cuidado.')
