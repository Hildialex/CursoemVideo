print('*¨¬'*15)
print('CAIXA ELETRÔNICO')
print('*¨¬'*15)
n1 = n2 = n3 = n4 = 0
while True:
    valor = int(input('Valor a sacar R$'))
    novo_valor = valor
    if valor >= 50:
        while valor >= 50:
            n1 += 1
            valor = valor - 50
    if valor >= 20:
        while valor >= 20:
            n2 += 1
            valor = valor - 20
    if valor >= 10:
        while valor >= 10:
            n3 += 1
            valor = valor - 10
    if valor >= 1:
        while valor >= 1:
            n4 += 1
            valor = valor - 1
    if valor == 0:
        break
print(f'O valor de R$ {novo_valor} sairá em:')
print(f'{n1} notas de R$ 50\n{n2} notas de R$ 20\n{n3} notas de R$ 10\n{n4} notas de R$ 1')
print('*¨¬'*15)
#* Solução Guanabara
# valor = int(input('Quanto sacar?'))
# total = valor
# ced = 50 AQUI RECEBE O VALOR DA MAIOR NOTA
# totCed = 0 PARA CONTAR QUANTAS CEDULAS
# while True:
#   if total >= ced:
#       total -= ced
#       totCed += 1
#   else:
#       if totCed > 0:
#           print(f'Total de {totCed} de R${ced}') MOSTRA APENAS CEDULAS COM QTD MAIOR QUE ZERO
#       if ced == 50:FAZ A TROCA DA CEDULA E DEPOIS VOLTA NO 1º IF(if total >= ced:)
#           ced = 20
#       if ced == 20:
#           ced = 10
#       if ced == 10:
#           ced = 1
#       if total == 0:
#           break