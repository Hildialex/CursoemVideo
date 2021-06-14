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
# Solução Guanabara
# def metade(preco=0, formato=False):
#   res = preco / 2
#   return res if not formato else moeda(res)
# 
# def dobro(preco=0, formato=False):
#   res = preco * 2
#   return res if formato is False else moeda(res)
