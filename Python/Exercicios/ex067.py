print('\033[36mTABAUADA\033[m')
cont = 0
while True:
    num = int(input('Quer saber a tabuada de qual valor?'))
    if num <= 0:
        print('Valor Inválido! Processo interrompido!')
        break
    print('=#='*10)
    print(f'\033[36mTabuada do {num}\033[m')
    while  cont <= 10:
        print(f'{num} X {cont} = {num*cont}')
        cont += 1
    cont = 0
    print('#=#'*10)