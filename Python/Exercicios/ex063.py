num = int(input('Digite um número:'))
a = fibo = 0
b = n = 1
while n < num:
    fibo = a + b
    print('{} ¬ {}'.format(b,fibo) if fibo == 1 else '{}'.format(fibo), end=' ¬ ')
    a = b
    b = fibo
    n += 1

