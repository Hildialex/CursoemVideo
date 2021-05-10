print('\033[36mÉ PRIMO?\033[m')
num = int(input('Digite o número:'))
s = 0
for i in range(1, num+1):
    if num%i == 0:
        s += 1
if s > 2 or s <= 1:
    print('\033[31mNÃO É PRIMO!\033[m')
else:
    print('\033[2;32mÉ NÚMERO PRIMO\033[m')
#*Solução Guanabara
#  tot = 0
#  num = int(input('Digite um número:'))
#  for c in range(1, num+1):
#   if num%c == 0:
#       print('\033[34m', end=' ')
#       tot += 1
#   else:
#       print('\033[31m', end=' ')
#  print('0 número {} foi divisível {} vezes'.format(num, tot)) 
#  if tot == 2:
#      print('E por isso ele É PRIMO!')
#  else:
#      print('E por isso ele NÃO É PRIMO!')
