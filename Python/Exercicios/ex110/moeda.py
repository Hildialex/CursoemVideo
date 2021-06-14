def moeda(n):
    return f'R$ {n:.2f}'.replace('.', ',')


def aumentar(n, p=0, formatar=False):
    valor = n + (n * (p/100))
    if formatar:
        return moeda(valor)
    return valor


def diminuir(n=0, p=0, formatar=False):
    valor = n - (n * (p/100))
    if formatar:
        return moeda(valor)
    return valor


def dobro(n=0, formatar=False):
    res = n*2
    if formatar:
        return moeda(res)
    return res


def metade(n=0, formatar=False):
    res = n/2
    if formatar:
        return moeda(res)
    return res


def resumo(preco=0, aumento=0, diminue=0):
    print('~'*25)
    print(f'{"RESUMO DO VALOR":>20}')
    print('~'*25)
    print(f'Preço Analizado:\t {moeda(preco):>15}')
    print(f'Dobro do preço:\t {dobro(preco, True):>15}')
    print(f'Metade do preço:\t {metade(preco, True):>15}')
    print(f'{aumento}% de aumento:\t {aumentar(preco, aumento, True):>15}')
    print(f'{diminue}% de redução:\t {diminuir(preco, diminue, True):>15}')
    print('~'*25)
