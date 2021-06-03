from time import sleep
def contador(inicio, fim, passo):
    if passo == 0:
        c = 1
    if passo < 0:
        c = passo * -1
    if passo > 0:
        c = passo
    print('-='*10)
    print(f'Contagem de {inicio} até {fim} de {passo} a {passo}')
    if inicio > fim and passo > 0:
        c = passo * -1
    else: 
        c = passo
    a = inicio
    b = fim
    for i in range(a, b+c, c):
        print(f'{i} ',end='', flush = True)
        sleep(0.3)
    print('FIM!')
    print('-=-'*10)

contador(1,10,1)
contador(10,0,2)
print('Agora é sua vez!')
ini = int(input('Início:'))
fim = int(input('Fim:'))
pas = int(input('Passo:'))
contador(ini, fim, pas)

# Solução Guanabara
# if p < 0: 
#   p *= -1
# if p == 0:
#   p = 1
# if i < f:
#   cont = 1
#   while cont <= f:
#       print(f'{cont}', end='', flush=True)
#       sleep(0.5)
#       cont += p
#   print('FIM!')
# else:
#   cont = i 
#   while cont >= f:
#       print(f'{cont}', end='', flush=True)
#       sleep(0.5)
#       cont -= p
#   print('FIM!')
#