print('{:=^40}'.format('LOJAS PYTHON'))
valor = float(input('Informe o valor do produto R$'))
condicao = int(input('''Informe a condição de pagamento:
[1]- À VISTA DINHEIRO
[2]- À VISTA CARTÃO
[3]- 2 VEZES CARTÃO
[4]- 3 OU MAIS VEZES
Opção:'''))
if condicao == 1:
    print('Sua compra possui 10% de desconto')
    print('Valor a pagar R${:.2f}'.format(valor*.9))
elif condicao == 2:
    print('Sua compra possui 5% de desconto')
    print('Valor a pagar R${:.2f}'.format(valor*.95))
elif condicao == 3:
    print('Sua compra não tem juros, será parcelada em 2X de R${:.2f}'.format(valor/2))
    print('Valor a pagar R${:.2f}'.format(valor))
elif condicao == 4:
    parc = int(input('Quantas parcelas?'))
    print('Sua compra possui 20% de juros, o valor das parcelas é R${:.2f}'.format(valor*1.2/parc))
    print('Valor a pagar R${:.2f}'.format(valor*1.2))
else:
    print('Opção inválida de pagamento, tente novamente')