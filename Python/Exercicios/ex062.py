termo = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão:'))
decimo = termo + (10-1) * razao
n = termo
z = 0
while n <= (decimo+razao):
    print ('{}'. format(n), end=' ¬ ')
    n += razao
    if n == (decimo+razao):
        novo = int(input('\nQuer mostrar mais termos? Digite o número de termos (0 para sair):'))
        if novo == 0:
            break
        else:
            z += novo
            decimo = termo + (10 + z - 1) * razao
