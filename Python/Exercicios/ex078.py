maior = menor = 0
lista = []
a = []
b = []
for  i in range(0,5):
    num = int(input('Digite um número:'))
    lista.append(num)
    if i == 0:
        maior = menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
for pos, i in enumerate(lista):
    if lista[pos] == maior:
        a.append(pos)
    elif lista[pos] == menor:
        b.append(pos)
print(f'O maior valor digitado foi {maior} nas posições {a}\nO menor valor foi {menor} nas posições {b}')
    

