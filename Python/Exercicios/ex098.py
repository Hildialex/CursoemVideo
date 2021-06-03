from time import sleep
def contador(inicio, fim, passo):
    print('A-', '-'*20)
    for i in range(1,11,1):
        print(f'{i} ', end='', flush=True)
        sleep(0.5)
    print('FIM')
    print('B-', '-'*20)
    for i in range(10,-1, -2):
        print(f'{i} ', end='', flush=True)
        sleep(0.5)
    print('FIM')
    print('C-', '-'*20)
    print('Agora sua vez de personalizar.')
    inicio = int(input('Início:'))
    fim = int(input('Fim:'))
    passo = int(input('Passo:'))
    if fim < inicio:
        if passo == 0:
            c = -1
        elif passo < 0:
            c = passo
        else:
            c = passo * -1
    else:
        c = passo
    a = inicio
    b = fim
    for i in range(a, b+c, c):
        print(f'{i} ',end='', flush = True)
        sleep(0.5)
    print('FIM')


contador(0,0,0)