n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro valor:'))
soma = n1+n2
print('A soma de {}{}{} e {}{}{} é igual a {}{}{}!'.format('\033[2;33m', n1 , '\033[m', '\033[2;33m', n2 , '\033[m', '\033[4;31m' , soma , '\033[m'))