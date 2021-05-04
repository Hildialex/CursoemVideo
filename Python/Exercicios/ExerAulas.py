import math
num = int(input('Digite um número:'))
raiz = math.sqrt(num)
print('A raiz de {} é: {:.2f}'.format(num, raiz))

#-----OUTRA MANEIRA-------
from math import sqrt, floor
num = int(input('Digite um número:'))
raiz = sqrt(num)
print('A raiz de {}  é: {:.2f}'.format(num, floor(raiz)))
#--------------------------

print('-----AULA09-------')
frase = 'Curso em Video Python'
print(frase[9])
print(frase[1:5])
print(frase[1:5:2])
print(frase[:9], frase[8:], frase[9::2])
print(frase.count('o'))
print(frase.find('de'))
print(frase.find('Android'))
print('Curso' in frase)
print(frase.replace('Python', 'Android'))
print(frase.upper(),'\n',frase.lower(),'\n',frase.capitalize())
print(frase.title(),'\nRemove espaços ante/depois',frase.strip(),'\nTemos tambem lstrip(), rstrip()')
print(frase.split(),'-'.join(frase))
print("""Nessa aula, vamos aprender operações com String no Python.
As principais operações que vamos aprender 
são o Fatiamento de String,
Análise com len(), count(), find(), 
ransformações com replace(), upper(), 
lower(), capitalize(), 
title(), strip(), junção com join().""")
#UMA STRING È IMUTÀVEL EM PYTHON
dividido = frase.split()
print(dividido,'\n', dividido[0],'\n',dividido[0][3])
print('----AULA 11-----')
print('\033[0;33;44m Mudando a cor!')
#\033[corresponde ao texto; cor do texto; cor do fundo ACABA COM LETRA 'M'

