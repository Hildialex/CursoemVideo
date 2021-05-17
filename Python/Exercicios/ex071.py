print('*¨¬'*15)
print('CAIXA ELETRÔNICO')
n1 = n2 = n3 = n4 = 0
while True:
    valor = int(input('Valor a sacar R$'))
    if valor >= 50:
        while valor-50 >= 50:
            n1 += 1
            print(n1)
        valor = valor - (n1*50)
        print('entrou aqui', valor)
    elif valor >= 20:
        while valor-20 >= 20:
            n2 += 1
        valor = valor - (n2*20)
    elif valor == 0:
        break
print(f'{n1} notas de R$50\n{n2} notas de R$20')