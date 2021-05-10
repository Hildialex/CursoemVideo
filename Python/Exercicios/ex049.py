print('\033[2;34;40mTABUADA COM FOR\033[m')
num = int(input('Digite um número para saber a tabuada:'))
print('{:=^40}'.format('=-'))
for i in range(0, 11):
    print('{} X {} = {}'.format(num, i, (num*i)))
print('{:=^40}'.format('=-'))