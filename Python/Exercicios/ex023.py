num = str(input('Digite um número de 0 à 9999:'))
novonum = '-'.join(num)
a = []
for i in novonum:
    if i != '-':
        a.append(i)
if len(num) == 4:
    print('Unidade:{}\nDezena:{}\nCentena:{}\nMilhar:{}'.format(a[3],a[2],a[1],a[0]))
if len(num) == 3:
    print('Unidade:{}\nDezena:{}\nCentena:{}'.format(a[2],a[1],a[0]))
if len(num) == 2:
    print('Unidade:{}\nDezena:{}'.format(a[1],a[0]))
if len(num) == 1:
    print('Unidade:{}'.format(a[0]))
#* O número tem que ser num = int(input(''))
# unidade = num // 1 % 10
# dezena = num // 10 % 10
# centena = num // 100 % 10
# milhar = num // 1000 % 10
*#