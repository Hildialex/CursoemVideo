from random import randint
tupla = ''
maior = menor = 0
for i in range(0,5):
    num = randint(0, 1000)
    if i == 0:
        maior = menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    tupla += ' '
    tupla += str(num)
print(f'A tupla é ({tupla})\nO maior número é: {maior}\nO menor número é: {menor}')
#* Solução Guanabara
#  n = (randint(1, 10), randint(1,10), randint(1, 10), randint(1,10), randint(1,10))
#  print(f'Os valores sorteados foram: {n}')
#  print(f'\nO maior valor:{max(n)}') 
#  print(f'O menor valor:{min(n)}')
# #