lista = list()
cont = 0
while True:
    lista.append(int(input('Digite um número:')))
    cont += 1
    lista.sort(reverse = True)
    resp = str(input('Deseja continuar?[s/n]')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Resposta Inválida! Deseja continuar?')).strip().upper()[0]
    if resp == 'N':
        break
print('-='*10)
print(f'Foram digitados {cont} valores.')
print(f'A lista informada decrescente é {lista}')
if 5 in lista:
    print('O número 5 está na lista!')
else:
    print('O número 5 NÃO está na lista!')

