lista = list()
for i in range (0,5):
    num = int(input('Digite o valor:'))
#Solução Guanabara
    if i == 0:
        lista.append(num)    
        print('Adicionado no começo')
    elif num > lista[(len(lista)-1)]:
        lista.append(num)
        print('Adicionado no final')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print('=-'*20)
print(f'Os valores da lista são: {lista}')