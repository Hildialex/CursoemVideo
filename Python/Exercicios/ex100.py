from random import randint
def sorteia(lst):
    for i in range(0,4):
        num = randint(1,100)
        lst.append(num)
    print(f'Os valores sorteados foram:{lst}')
def somaPar(lst):
    soma = 0
    for i in lst:
        if i%2 == 0:
            print(f'{i} ->', end='')
            soma += i
    print(f'A soma dos números pares é {soma}')
numeros = list()
sorteia(numeros)
somaPar(numeros)