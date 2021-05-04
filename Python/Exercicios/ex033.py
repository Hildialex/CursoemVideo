num1 = int(input('Informe um número:'))
num2 = int(input('Informe o segundo número:'))
num3 = int(input('Informe o terceiro número:'))
print('Analizando números informados...')
if num3 < num1 > num2:
    if num2 > num3:
        a = num3
    else:
        a = num2
    print('O MAIOR entre eles é:{}\nE o MENOR é:{}'.format(num1, a))
if num3 < num2 > num1:
    if num1 > num3:
        a = num3
    else:
        a = num1
    print('O MAIOR entre eles é:{}\nE o MENOR é:{}'.format(num2, a))
if num1 < num3 > num2:
    if num1 > num2:
        a = num2
    else:
        a = num1
    print('O MAIOR entre eles é:{}\nE o MENOR é:{}'.format(num3, a))

