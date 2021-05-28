lista = list()
pares = []
impares = []
for cont in range(0,7):
    num = int(input(f'Digite o {cont+1}º valor:'))
    if num%2 == 0:
        pares.append(num)
    elif num%2 == 1:
        impares.append(num)
lista.append(pares[:])
lista.append(impares[:])
lista[0].sort()
lista[1].sort()
print('=-'*15)
print(f'Os valores pares digitados foram {lista[0]}')
print(f'Os valores impares digitados foram {lista[1]}')
#* Solução Guanabara
# num = [[],[]]
# valor = 0
# for c in range(1,8):
#   valor = int(input('Digite um valor:'))
#   if valor%2 == 0:
#       num[0].append(valor)
#   else:
#       num[1].append(valor)
# num[0].sort()
# num[1].sort()
# #
