print('Formas de pagamento')
valor = float(input('Informe o valor do produto R$'))
condicao = int(input('Informe a condição de pagamento:\n1-À VISTA DINHEIRO\n2-À VISTA CARTÃO\n3- 2 VEZES CARTÃO\n4- 3 OU MAIS VEZES\n'))
if condicao == 1:
    print('Valor a pagar R${:.2f}'.format(valor*.9))
elif condicao == 2:
    print('Valor a pagar R${:.2f}'.format(valor*.95))
elif condicao == 3:
    print('Valor a pagar R${:.2f}'.format(valor))
else:
    print('Valor a pagar R${:.2f}'.format(valor*1.2))
