print('\033[7;31;40mSOMANDO PARES\033[m')
s = 0
for i in range(0,6):
    num = int(input('Digite um número:'))
    if num%2 == 0:
        s += num
print('\033[34mA soma dos pares é:{}\033[m'.format(s))

    