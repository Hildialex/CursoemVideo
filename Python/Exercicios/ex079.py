lista = []
cont = 0
while True:
    num = (int(input('Digite um número:')))
    if cont == 0:
        lista.append(num)
    a = num
    resp = str(input('Deseja continuar?[s/n]')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Resposta Inválida!Deseja continuar[s/n]?')).strip().upper()[0]
    if resp == 'N':
       break
print(lista)