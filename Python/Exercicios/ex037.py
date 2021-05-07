print('\033[4;32mLendo números e convertendo\033[m')
num = int(input('Digite um número inteiro:'))
base = int(input('Qual a base de conversão?\n1-Binário\n2-Octal\n3-Hexadecimal\n'))
if base == 1:
    resp = bin(num)
    print('O número {}{}{} em binário é:{}{}{}'.format('\033[34m', num, '\033[m', '\033[35m', resp[2:], '\033[m'))
elif base == 2:
    resp = oct(num)
    print('O número {}{}{} em octal é:{}{}{}'.format('\033[34m', num, '\033[m', '\033[35m', resp[2:], '\033[m'))
else:
    resp = hex(num)
    print('O número {}{}{} em hexadecimal é:{}{}{}'.format('\033[34m', num, '\033[m', '\033[35m', resp[2:], '\033[m'))



