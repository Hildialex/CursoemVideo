num = int(input('Digite um número:'))
n = 0
f = 1
while n < num:
    n += 1
    print('{}'.format(f), end=' ¬ ')
    f = (f + n) - f
