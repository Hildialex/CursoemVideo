print('\033[4;31;40m Comparando números\033[m')
num = int(input('Digite o primeiro número inteiro:'))
num2 = int(input('Digite o segundo número:'))
if num > num2:
    print('\033[33m O primeiro número é MAIOR!\033[m')
elif num < num2:
    print('\033[32m O segundo número é MAIOR!\033[m')
else:
    print('\033[36m Ambos são iguais!\033[m')