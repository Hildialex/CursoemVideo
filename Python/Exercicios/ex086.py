matriz = list()
for linha in range(0,3):
    num = []
    for coluna in range(0,3):
       num.append(int(input(f'Digite um valor para [{linha}, {coluna}]:')))
    matriz.append(num[:])
    num.clear()
print('=-='*15)
#Acesso direto ao conteudo de cada linha, colocando um indice para cada coluna
for val, val1, val2 in matriz:
    print(f'[ {val} ]  [ {val1} ]  [ {val2} ]')
#* Solução Guanabara
# matriz = [[0,0,0],[0,0,0],[0,0,0]]
# for l range(0,3):
#   for c in range(0,3):
#       matriz[l][c] = int(input(f'Digite o valor de [{l}, {c}]'))
# print('=-'*30)
# for l in range(0,3):
#   for c in range(0,3):
#       print(f'[{matriz[l][c]:^5}]', end='')
#   print()
# #