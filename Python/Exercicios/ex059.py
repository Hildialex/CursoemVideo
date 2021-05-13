op = 0
while op != 5:
    num1 = int(input('Digite o Primeiro número:'))
    num2 =int(input('Digite o Segundo número:'))
    print('''\033[4;36mMENU\033[m
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAOIR
    [4] NOVOS NÚMEROS
    [5] SAIR''')
    op = int(input(''))
    if op == 1:
        print('A soma de {} e {} é:{}'.format(num1, num2, num1+num2))
    elif op == 2:
        print('A multiplicação de {} por {} é:{}'.format(num1, num2, num1*num2))
    elif op == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('O maior entre {} e {} é:{}'.format(num1, num2, maior))
    elif op == 4 or op == 5:
        continue
    else:
        print('Opção Inválida! Tente novamente.')
