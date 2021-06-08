def leiaInt(n):
    """
    -> Verifica se o valor informado e numero
    """
    num = str(input(n))
    if num.isnumeric():
        num = int(num)
        return num
    else:
        print('\033[0:31m ERRO! Digite um número inteiro válido.')
num = leiaInt('Digite um número:')
print(f'O número digitado foi {num}')
# Solução Guanabara
# def leiaInt(msg):
#   ok = False
#   valor = 0
#   while True:
#       n = str(input(msg))
#       if n.isnumeric():
#           valor = int(n)
#           ok = True
#       else:
#           print('\033[0:31m ERRO Digite um número inteiro válido!')
#       if ok:
#           break
#   return valor