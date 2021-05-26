lista = list()
par = []
impar = []
while True:
    lista.append(int(input('Digite um número:')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [s/n]?')).strip().upper()[0]
    if resp == 'N':
        break
for i in lista:
    if i%2 == 0:
        par.append(i)
    elif i%2 == 1:
        impar.append(i)
print('*'*10)
print(f'''Você digitou os valores {lista}
        A lista com os números pares é {par}
        A lista com números impares é {impar}''')
        