print('-'*45)
x = 'Calculando o peso ideal.'
print(f'{x:^45}')
print('-'*45)

altura = float(input('Sua altura em metros: '))
peso = float(input('Seu peso em quilogramas: '))
imc = peso / (altura*altura)
if imc < 18.5:
    print('De acorodo com os dados informados você está abaixo do peso!')
elif 18.5 <= imc <= 25:
    print('De acordo com os dados informados você está no peso ideal!')
elif 25 < imc <= 30:
    print('De acordo com os dados informados você está sobrepeso!')
elif 30 < imc <= 40:
    print('De acordo com os dados informados você está obeso!')
else:
    print('De acordo com os dados informados você está em obesidade morbida!')
