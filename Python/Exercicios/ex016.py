import math
num = float(input('Digite um número qualquer:'))
print('A parte inteira de {} é: {}'.format(num, math.ceil(num-1)))
#Solução guanabara math.trunc(num) corta parte inteira
#Sem lib: usar a função int(num)