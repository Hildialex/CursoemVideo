lista = list()
for i in range (0,5):
    num = int(input('Digite o valor:'))
    if len(lista) == 0:
        lista.append(num)
    elif num < lista[0]:
        lista.insert(0,num)
    elif num > lista[0]:
        lista.insert(i,num)
print(f'A lista ordenada sem sort() é {lista}')
