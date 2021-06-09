def moeda(n):
    return f'R$ {n:.2f}'.replace('.', ',')


def aumentar(n, p=0):
    valor = n + (n * (p/100))
    return valor


def diminuir(n=0, p=0):
    valor = n - (n * (p/100))
    return valor


def dobro(n=0):
    res = n*2
    return res


def metade(n=0):
    res = n/2
    return res
