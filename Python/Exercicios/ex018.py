import math
num = float(input('Digite o ângulo:'))
num1 = math.radians(num)
print('O ângulo {}, possui seno de {:.2f}\n cosseno de {:.2f}\n e tangente {:.2f}'.format(num, math.sin(num1), math.cos(num1), math.tan(num1)))
#Solução guanabara sen = math.sin(math.radians(num))