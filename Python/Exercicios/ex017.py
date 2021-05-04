import math
catop = float(input('Digite o valor do cateto oposto:'))
catad = float(input('Digite o valor do cateto adjacente:'))
hipo = math.sqrt(math.pow(catop,2)+math.pow(catad,2))
print('O comprimento da hipotenusa é de {:.1f}'.format(hipo))
#Solução guanabara: ((catop**2)+(catop**2))**0.5 ou math.hypot(catop, catad)