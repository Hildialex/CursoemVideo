lista = list()
while True:
    num = int(input('Digite um número:'))
    if len(lista) == 0 or num not in lista:
        lista.append(num)
        print('Adicionado com sucesso!')
    elif num in lista:
        print('Valor Duplicado! Não vou adicionar...')
    resp = str(input('Deseja continuar?[s/n]')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Resposta Inválida!Deseja continuar[s/n]?')).strip().upper()[0]
    if resp == 'N':
       break
    lista.sort()
print(f'A lista formada é {lista}')
