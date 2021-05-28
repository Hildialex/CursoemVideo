matriz = list()
par = terceira = maior = 0
for linha in range(0,3):
    num = []
    for coluna in range(0,3):
        num.append(int(input(f'Digite um valor para [{linha}, {coluna}]:')))
        if num[coluna]%2 == 0:
            par += num[coluna]
        if coluna == 2:
            terceira += num[coluna]
        if linha == 1:
            if coluna == 0:
                maior = num[coluna]
            elif num[coluna] > maior:
                maior = num[coluna]
    matriz.append(num[:])
    num.clear()
print('=-='*15)
for var, var1, var2 in matriz:
    print(f'[ {var} ]  [ {var1} ]  [ {var2} ]')
print('=-='*15)
print(f'A soma dos valores pares: {par}')
print(f'A soma dos valores da terceira coluna: {terceira}')
print(f'O maior valor da segunda linha: {maior}')