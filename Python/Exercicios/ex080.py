lista = list()
for i in range (0,5):
    num = int(input('Digite o valor:'))
    if len(lista) == 0:
        lista.append(num)
    else:
        cont = 0
        while cont < len(lista):
            if num < lista[cont]:
                lista.insert(cont, num)
        
print(f'A lista ordenada sem sort() é {lista}')
