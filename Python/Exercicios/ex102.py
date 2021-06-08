def fatorial(n, show = False):
    """
    ->Calcula o fatorial de um numero.
    param n: O numero a ser calculado
    param show: (opcional) Mostrar ou nao a conta.
    return: O valor do fatorial de um numero n.
    """
    f = 1
    conta = ''
    for c in range(n, 0, -1):
        if c == 1:
            conta += f'{c} = {f}'
        else:
            conta += f'{c} X '
        f *= c
    if show:
        return conta
    else:
        return f
print(fatorial(5))
print(fatorial(5, False))
print(fatorial(5, True))
help(fatorial)
# Solução Guanabara
# def fatorial(n, show=False):
#   f = 1
#   for c in range(n, 0, -1):
#      if show:
#           print(c, end='')
#           if c > 1:
#               print(' X ', end='') 
#           else:
#               print(' = ', end='')
#      f *= c
#   return f
