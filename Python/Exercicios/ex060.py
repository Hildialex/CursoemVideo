print('\033[7;30;40mFATORIAL\033[m')
num = int(input('Digite um número:'))
n = 0
while n != num:
    n += 1
    fato = n +(n * num)
print('O fatorial de {}! é: {}'.format(n,fato))