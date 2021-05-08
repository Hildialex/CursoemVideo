print('\033[4;35m EMPRÉSTIMO BANCÁRIO\033[m')
valor = float(input('Digite o valor da casa R$'))
sal = float(input('Digite o salário R$'))
qtd = float(input('Digite a quantidade de anos à pagar:'))
parcela = valor / (qtd*12)
limite = sal * 0.7
if limite <= parcela:
    print('O valor das parcelas é de R$\033[2;33m{:.2f}\033[m\nVocê \033[2;31mNão\033[m foi aprovado para o empréstimo!'.format(parcela))
else:
    print('Empréstimo \033[34mAprovado\033[m\nO valor das parcelas é de R$\033[2;33m{:.2f}'.format(parcela))