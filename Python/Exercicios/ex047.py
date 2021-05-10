print('\033[4;32mSÓ PARES\033[m')
for i in range(0, 51, 2):
    if i != 0:
        print(i)

#também da assim
for i in range(1, 51, 2):
    print(i+1)

#Solução guanabara
for i in range(2,51,2):
    print(i)
for i in range(1, 51):
    if i%2 == 0:
        print(i)