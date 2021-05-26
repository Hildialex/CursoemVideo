lista = list()
for  i in range(0,5):
    num = int(input(f'Digite um número para a posição {i}:'))
    lista.append(num)
maior = max(lista)
menor = min(lista)
resp = resp1 = ''
print('+=-'*20)
print(f'Você digitou os valores {lista}')
print('+=-'*20)
for pos, i in enumerate(lista):
    if i == maior:
        resp += (str(pos) + '...')
    elif i == menor:
        resp1 += (str(pos) +'...')
print(f'O maior valor digitado foi {maior} nas posições {resp}')
print(f'O menor valor digitado foi {menor} nas posições {resp1}')

#* Solução Guanabara
# print(f'O maoir valor foi {maior} nas posiçoes ', end ='')
# for i,v in enumerate(lista):
#   if v == maior:
#       print(f'{i}...', end='')
# print(f'O menor valor foi {menor} nas posições ', end='')
# for i, v in enumerate(lista): 
#   if v == menor:
#       print(f'{i}...', end='')
# #