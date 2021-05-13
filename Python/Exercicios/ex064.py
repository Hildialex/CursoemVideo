n = i = soma = 0
while n != 999:
    num = int(input('Digite um número(999 para sair):'))
    n = num
    i += 1
    if n != 999:
        soma += num
print('A soma dos {} números digitados é {}'.format(i-1, soma))