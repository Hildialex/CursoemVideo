item = ('Pão', 3.5, 'Leite', 3.45, 'Café', 8.79, 'Arroz', 12.59, 'Feijão', 5.69, 'Trigo', 3.49, 'Bolacha Trakinas', 1.19)
print('-'*40)
print('{:^40}'.format('Listagem de Preços'))
print('-'*40)
for pos in range(0, len(item)):
    if pos%2 == 0:
        print(f"{item[pos]}","."*20,f"R$ {float(item[pos+1]):.2f}")
print('-'*40)
#Solução Guanabara
# print('-'*40)
# print(f'{"Listagem de Preços":^40}')
# print('-'*40)
# for pos in range(0, len(lista)):
#   if pos%2 == 0:
#       print(f'{lista[pos]:.<40}', end='')
#   else:
#       print(f'R${lista[pos]:>5.2f})