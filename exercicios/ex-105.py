def notas(*n, sit=False):
    """
    ->Função para análise de notas de vários alunos:
    :param n: uma ou mais notas.
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: Dicionário com várias informações.
    """
    print(n)
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'Boa'
        elif r['media'] >= 5:
            r['situação'] = 'Razoavel'
        else:
            r['situação'] = 'Ruim'
    return r


resp = notas(4, 8.5, 9.3, sit=True)
print(resp)
