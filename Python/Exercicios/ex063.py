num = int(input('Digite um número:'))
a = fibo = 0
b = n = 1
while n < num:
    fibo = a + b
    print('{} ¬ {}'.format(b,fibo) if fibo == 1 else '{}'.format(fibo), end=' ¬ ')
    a = b
    b = fibo
    n += 1
print('FIM')
#*SOLUÇÃO GUANABARA
#  n = int(input('Qunatos termos voce quer mostar?'))
#  t1 = 0
#  t2 = 1
#  print('~'*30)
#  print('{} ¬ {}'.format(t1, t2), end =' ')
#  cont = 3
#  while cont <= n:
#   t3 = t1 + t2
#   print('¬ {}'.format(t3), end =' ')
#   t1 = t2
#   t2 = t3
#   cont += 1
# print('FIM')
# #
