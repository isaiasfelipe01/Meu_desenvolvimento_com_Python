preço = float(input('Qual o preço do produto? R$'))
print(f'O produto que custava R${preço:.2f}, na promoção com 5% de desconto vai custar R${preço-((preço*5)/100):.2f}.')
