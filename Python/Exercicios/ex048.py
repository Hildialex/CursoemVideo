print('\033[31mMÚLTIPLOS DE 3!\033[m')
s= 0 
cont = 0
for i in range(1, 501, 2):
    if i%3 == 0:
        s += i
        cont += 1
print('A soma de {} múltiplos de 3 é:{}'.format(cont, s))
