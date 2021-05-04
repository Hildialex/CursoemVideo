sal = float(input('Informe seu salário R$'))
print('Calculando seu aumento ...')
if sal <= 1250:
    print('Seu salário de R${:.2f} passa a ser R${:.2f}'.format(sal, sal*1.15))
else:
    print('Seu salário de R${:.2f} passa a ser R${:.2f}'.format(sal, sal*1.10))

