print('\033[7;30;40mFATORIAL\033[m')
num = int(input('Digite um número:'))
n = num
facto = 1
while n > 1:
    facto *= n
    n -= 1
print('O fatorial de {}! é: {}'.format(num, facto))
print('**' * 4)
facto = 1
for i in range(num, 0, -1):
    print('Fatorial de {}!'.format(i), end='')
    print(' X ' if i > 1 else '=', end='')
    facto *= i
print(' = {}'.format(facto))
#* Solução Guanabara
# from math import factorial
# n = int(input('Digite um número:'))
# resp = factorial(n)
# print('Fatorial de {} é {}':.format(n, resp))
# 
# n = int(input('Digite um número'))
# c = n
# f = 1
# while c > 0 :
#   print('{}'.format(c), end=' ')
#   print(' X ' if c > 1 else ' = ', end=' ')
#   f *= c
#   c -= 1
# print('{}'.format(f))
# #