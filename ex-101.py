def voto(ano):
    from datetime import date
    atual = date.today().year
    x = atual - ano
    if x < 16:
        return f'Com {x} anos: VOTO NEGADO!'
    if 16 <= x < 18 or x > 65:
        return f'Com {x} anos: VOTO OPCIONAL!'
    else:
        return f'Com {x} anos: VOTO OBRIGATORIO!'


print('-'*30)
nasc = int(input('Em qual ano você nasceu? '))
print(voto(nasc))
